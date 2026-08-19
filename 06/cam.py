import cv2

# Підключаємо камеру
cap = cv2.VideoCapture(0)
print("📷 Запускаю камеру... Натисни 'q' (англійську), щоб вийти.")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Не вдалося захопити відео.")
        break

    # 1. Перетворюємо кадр на чорно-білий
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Магія OpenCV: алгоритм Canny шукає різкі переходи (контури)
    edges = cv2.Canny(gray, 10, 10)

    # Показуємо результат
    cv2.imshow('OpenCV Matrix Effect', edges)

    # Чекаємо натискання 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()