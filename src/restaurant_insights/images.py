from pathlib import Path


def image_features(path: str | Path) -> dict[str, float | int]:
    from PIL import Image, ImageStat

    with Image.open(path) as image:
        rgb = image.convert("RGB")
        width, height = rgb.size
        brightness = sum(ImageStat.Stat(rgb).mean) / 3
    return {
        "width": width,
        "height": height,
        "aspect_ratio": round(width / height, 3),
        "brightness": round(brightness, 2),
    }
