#%%
import cv2
# hi = cv2.imread("test.png")
# hi
# # %%
# hi = cv2.cvtColor(hi, cv2.COLOR_BGR2BGR)
# hi.shape
# # %%
# cv2.imshow('image',hi)
# #%%
# cv2.waitKey(0)
# # %%

# cv2.destroyAllWindows()
# %%
cap = cv2.VideoCapture(0)
# %%
# # %%
# cap.__dir__()
# %%
print(cap.isOpened())
# cap.release()
#%%
cap.open()
# %%
cap.set(3,320)
# %%
cap.set(4,240)
# # %%
# cap.set(4,240)
# # %%
# cv2.__version__
# %%
while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xff == ord('w'):
            break


cv2.destroyAllWindows()

# %%
