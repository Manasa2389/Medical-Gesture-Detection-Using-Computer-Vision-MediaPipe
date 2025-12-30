import cv2
import mediapipe as mp

# ---------------- MediaPipe Setup ----------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ---------------- Camera ----------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

# ---------------- Gesture Logic ----------------
def detect_gesture(lm):
    wrist = lm[0]

    thumb_tip = lm[4]
    thumb_ip = lm[3]

    index_tip, index_pip = lm[8], lm[6]
    middle_tip, middle_pip = lm[12], lm[10]
    ring_tip, ring_pip = lm[16], lm[14]
    pinky_tip, pinky_pip = lm[20], lm[18]

    fingers_up = [
        index_tip.y < index_pip.y,
        middle_tip.y < middle_pip.y,
        ring_tip.y < ring_pip.y,
        pinky_tip.y < pinky_pip.y
    ]

    # ✋ HELP (Open Palm)
    if all(fingers_up):
        return "HELP ✋"

    # ✊ PAIN (Fist)
    if not any(fingers_up) and thumb_tip.y > wrist.y:
        return "PAIN ✊"

    # ☝ WATER (Index Finger)
    if fingers_up[0] and not any(fingers_up[1:]):
        return "WATER ☝"

    # ✌ FOOD (Two Fingers)
    if fingers_up[0] and fingers_up[1] and not any(fingers_up[2:]):
        return "FOOD ✌"

    # 👍 EMERGENCY (Thumb Up) ✅ FIXED
    if (
        thumb_tip.y < thumb_ip.y and
        not any(fingers_up)
    ):
        return "EMERGENCY 👍"

    return "UNKNOWN"

# ---------------- Full Screen Window ----------------
window_name = "Medical Gesture Detection"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(
    window_name,
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

# ---------------- Main Loop ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    label = "No Hand Detected"

    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_lms,
                mp_hands.HAND_CONNECTIONS
            )
            label = detect_gesture(hand_lms.landmark)

    # ---------------- UI ----------------
    cv2.rectangle(frame, (30, 30), (800, 120), (0, 0, 0), -1)
    cv2.putText(
        frame,
        label,
        (50, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (0, 255, 0),
        4
    )

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()