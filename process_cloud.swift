import Cocoa
import CoreGraphics
import Foundation

let inputPath = "/Users/michellemiyata/.gemini/antigravity/brain/fd7541c9-196b-408c-a300-0542a70db05b/.user_uploaded/media_1788454318637.png"
let outputPath = "/Users/michellemiyata/Downloads/portfolio-main/cloud_mark_transparent.png"

guard let image = NSImage(contentsOfFile: inputPath),
      let tiffData = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiffData),
      let cgImage = bitmap.cgImage else {
    print("Failed to load image")
    exit(1)
}

let width = cgImage.width
let height = cgImage.height

// Crop out the bottom text "2) SINGLE-LINE CLOUD MIST." (keep only the cloud emblem at top)
// The text is in the lower ~25% of the image
let cropRect = CGRect(x: 0, y: Int(Double(height) * 0.22), width: width, height: Int(Double(height) * 0.78))
guard let croppedCG = cgImage.cropping(to: cropRect) else {
    print("Crop failed")
    exit(1)
}

let cWidth = croppedCG.width
let cHeight = croppedCG.height

// Create RGBA bitmap context to remove off-white background and make it pure transparent
let colorSpace = CGColorSpaceCreateDeviceRGB()
let bytesPerPixel = 4
let bytesPerRow = bytesPerPixel * cWidth
let rawData = UnsafeMutablePointer<UInt8>.allocate(capacity: cHeight * bytesPerRow)

guard let context = CGContext(data: rawData,
                              width: cWidth,
                              height: cHeight,
                              bitsPerComponent: 8,
                              bytesPerRow: bytesPerRow,
                              space: colorSpace,
                              bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue) else {
    print("Context failed")
    exit(1)
}

context.draw(croppedCG, in: CGRect(x: 0, y: 0, width: cWidth, height: cHeight))

// Process pixels: background is warm off-white (#FDFBF7 ~ 253, 251, 247)
// Stroke is terracotta rose (#B28F81 ~ 178, 143, 129)
for y in 0..<cHeight {
    for x in 0..<cWidth {
        let byteIndex = (y * bytesPerRow) + (x * bytesPerPixel)
        let r = Double(rawData[byteIndex])
        let g = Double(rawData[byteIndex + 1])
        let b = Double(rawData[byteIndex + 2])
        
        // Luminance / lightness
        let lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
        
        // Background is around lum > 0.92
        // We calculate alpha based on how dark it is compared to background
        if lum > 0.94 {
            rawData[byteIndex + 3] = 0 // fully transparent
        } else if lum < 0.70 {
            rawData[byteIndex + 3] = 255 // fully opaque
            // Normalize stroke color to rich terracotta #B28F81 (178, 143, 129)
            rawData[byteIndex] = 178
            rawData[byteIndex + 1] = 143
            rawData[byteIndex + 2] = 129
        } else {
            // Smooth anti-aliased edge
            let alpha = UInt8((1.0 - (lum - 0.70) / (0.94 - 0.70)) * 255.0)
            rawData[byteIndex + 3] = alpha
            rawData[byteIndex] = 178
            rawData[byteIndex + 1] = 143
            rawData[byteIndex + 2] = 129
        }
    }
}

guard let outCG = context.makeImage() else {
    print("Output image failed")
    exit(1)
}

let outBitmap = NSBitmapImageRep(cgImage: outCG)
guard let pngData = outBitmap.representation(using: .png, properties: [:]) else {
    print("PNG conversion failed")
    exit(1)
}

try pngData.write(to: URL(fileURLWithPath: outputPath))
print("Successfully created transparent cloud mark at \(outputPath)")
