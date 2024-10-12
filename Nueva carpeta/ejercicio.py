from PIL import Image
imagen = Image.new('RGB',(100, 100), color='red')

imagen.save('imagen_roja.png')

print("imagen creada 'imagen_roja.png'")