def optimize_image(sender, instance, **kwargs):
    if instance.cover:
        from PIL import Image
        image = Image.open(instance.cover.path)
        image.save(instance.cover.path, quality=20, optimize=True)
