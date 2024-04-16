import cv2
import numpy as np
 
# Carrega uma imagem
# Neste caso estamos criando uma imagem RGB preta de tamanho 480x640
img = np.zeros((480, 640, 3), dtype="uint8")
  
# Exibe a imagem
cv2.imshow('image', img)

# Variável de controle para verificar se o botão do mouse está pressionado
mouse_pressed = False

# Função de callback, quando ocorre um evento do mouse, essa função é chamada
def mouse_click(event, x, y, flags, param):
    global mouse_pressed
    
    # Se foi pressionado o botão esquerdo do mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
    
    # Se o botão do mouse estiver pressionado e houver movimento do mouse
    if event == cv2.EVENT_MOUSEMOVE and mouse_pressed:
        # Realiza função... 
        cv2.circle(img, (x,y), 20, (0,255,0), -1)
        cv2.imshow('image', img)
    
    # Se o botão do mouse foi solto
    if event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False


# Seta a função de callback que será chamada 
# Evento 'image', função callback mouse_click  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)
  
# fecha a janela.
cv2.destroyAllWindows()
