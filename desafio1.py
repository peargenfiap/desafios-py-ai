import cv2
import numpy as np
 
# Carrega uma imagem
# Neste caso estamos criando uma imagem RGB preta de tamanho 480x640
img = np.zeros((480, 640, 3), dtype="uint8")
  
# Exibe a imagem
cv2.imshow('image', img)

# Função de callback, quando ocorre um evento do mouse, essa função é chamada
def mouse_click(event, x, y, flags, param):
    global img
    # Se foi o botão esquerdo do mouse  


    # Se foi o botão direito do mouse  
    if event == cv2.EVENT_RBUTTONDOWN:
        
        # ---------- implemente a solução... 
        img[:,:] = [255,0,0]

        cv2.imshow('image', img)
    # Se foi o botão direito do mouse  

    if event == cv2.EVENT_LBUTTONDBLCLK:
        
        # ---------- implemente a solução... 
        img[:,:] = [0,0,255]

        cv2.imshow('image', img)

    if event == cv2.EVENT_MBUTTONDBLCLK:
        
        # ---------- implemente a solução... 
        img[:,:] = [0,255,0]

        cv2.imshow('image', img)



# Seta a função de callback que será chamada 
# Evento 'image', função callback mouse_click  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)
  
# fecha a janela.
cv2.destroyAllWindows()