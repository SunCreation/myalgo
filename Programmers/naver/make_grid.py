#%%
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
from time import sleep, time

from pyparsing import alphas
from grid_diagonal import solution

def fig2array(fig):
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)

def point(draw, *posis, size=5, color=(210,20,250)):
    if posis is None:
        raise ValueError("Experted argument 'posis' is not given")
    for pos in posis:
        # 점 찍어주는 것은 x,y 좌표가 생각과 다르기 때문에, 순서를 뒤집는다.
        y,x = pos
        draw.ellipse((x_ticks[x]-size,y_ticks[y]-size,x_ticks[x]+size,y_ticks[y]+size),fill=color )


if __name__ == '__main__':
    sys.stdin = open("data")
    grid = eval(sys.stdin.readline())
    print(grid)
    height = 600
    width = 600
    N = len(grid)
    image = Image.new(mode='P', size=(height, width), color=255)
    # Draw some lines
    draw = ImageDraw.Draw(image)
    # plt.imshow(image)
    offset = 20
    y_start = offset
    y_end = image.height - offset
    x_start = offset
    x_end = image.width - offset
    step_size = int((x_end - offset) / N)
    x_ticks = []
    y_ticks = []

    for x in range(offset, x_end+1, step_size):
        x_ticks.append(x)
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=(28,28,28))
    for y in range(offset,y_end+1, step_size):
        y_ticks.append(y)
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=(28,28,28))
    for j, line in enumerate(grid):
        for i, pos in enumerate(line):
            if pos==0:
                line = ((x_ticks[i],y_ticks[j]),(x_ticks[i+1],y_ticks[j+1]))
                draw.line(line, fill=(28,28,28))
            if pos==1:
                line = ((x_ticks[i],y_ticks[j+1]),(x_ticks[i+1],y_ticks[j]))
                draw.line(line, fill=(28,28,28))
    # 예시
    # point(draw, (0,4))
    # point(draw, (1,3))
    # point(draw, (2,2))
    # point(draw, (3,1))
    # point(draw, (4,0))

    # del draw
    f = plt.figure()
    plt.imshow(image)
    plt.axis('off')
    plt.savefig('hihi.png')

    # print(fig2array((f)))
    hi = fig2array((f))#np.asarray(image)

    while True:
        for posis in (list(zip(range(5), i)) for i in solution(grid)):
            st = time()
            while True:
                pallets = [image.copy() for i in range(3)]
                draws = [ImageDraw.Draw(pallet) for pallet in pallets]
                t = time() - st
                point(draws[2], *posis, color=255+int(160*t*(t-2)))
                point(draws[1], *posis, color=255+int(160*t*(t-2)))
                # point(draws[2], *posis, color=255+int(150*t*(t-2)))

                # f = plt.figure()
                # plt.imshow(pallet)
                # plt.axis('off')
                # pallet = fig2array(f)
                # print(pallet)
                # print(np.array(pallet).shape)

                c_pallet = np.stack([np.array(pallet) for pallet in pallets], axis=-1)
                cv2.imshow("test",c_pallet)
                # pallet = image.copy()
                # sleep(10)
                # f = plt.figure()
                # plt.imshow(pallet)
                # plt.axis('off')
                # pallet = fig2array(f)
                # cv2.imshow("test",pallet)
                if cv2.waitKey(1) & 0xff == ord('w') or t > 2:
                    break

        sleep(3)
        break
    cv2.destroyAllWindows()
    # print(hi)
    # plt.show()


# %%
