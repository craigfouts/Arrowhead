import cv2
import mediapipe as mp

class HandTracker:
    """TODO
    
    Parameters
    ----------
        n_hands : int, default=2
            TODO
    
    Attributes
    ----------
        hands_ : TODO
            TODO
        landmarks_ : TODO
            TODO
    """

    def __init__(self, n_hands=2):
        self.n_hands = 2
        
        self.hands_ = mp.solutions.hands
        self.landmarks_ = None

    def find_hands(self, img, draw=True):
        """TODO
        
        Parameters
        ----------
            img : TODO
                TODO
            draw : bool, default=True
                TODO
        
        Returns
        -------
            img : TODO
                TODO
        """

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.landmarks_ = self.hands.process(img).multi_hand_landmarks
        
        if draw and self.landmarks:
            mp_draw = mp.solutions.drawing_utils

            for landmark in self.landmarks:
                connections = self.mp_hands.HAND_CONNECTIONS
                mp_draw.draw_landmarks(img, landmark, connections)
        
        return img
    
    def find_landmarks(self, img, hand_idx=0, landmark_ids=(), r=10, c=(255, 0, 0)):
        """TODO
        
        Parameters
        ----------
            img : TODO
                TODO
            hand_idx : int, default=0
                TODO
            landmark_ids : tuple, default=()
                TODO

        Returns
        -------
            landmarks : list
                TODO
        """

        landmarks = []

        if self.landmarks_:
            hand = self.landmarks_[hand_idx]

            for id, landmark in enumerate(hand.landmark):
                h, w = img.shape[:2]
                x, y = int(landmark.x*w), int(landmark.y*h)
                landmarks.append([id, x, y])

                if id in landmark_ids:
                    cv2.circle(img, (x, y), r, c, cv2.FILLED)
        
        return landmarks
