#%%
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
from grid_diagonal import solution
sys.stdin = open("data")

def fig2array(fig):
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)

def point(draw, pos=None, size=5, color=(210,20,250)):
    if pos is None:
        raise ValueError("Experted argument 'pos' is not given")
    x,y = pos
    draw.ellipse((x_ticks[x]-size,y_ticks[y]-size,x_ticks[x]+size,y_ticks[y]+size),fill=color)


if __name__ == '__main__':
    height = 600
    width = 600
    image = Image.new(mode='P', size=(height, width), color=255)
    # Draw some lines
    draw = ImageDraw.Draw(image)
    offset = 20
    y_start = offset
    y_end = image.height - offset
    x_start = offset
    x_end = image.width - offset
    step_size = int((x_end - offset) / 4)
    x_ticks = []
    y_ticks = []

    for x in range(offset, x_end+1, step_size):
        x_ticks.append(x)
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=28)
    for y in range(offset,y_end+1, step_size):
        y_ticks.append(y)
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=28)
    grid = eval(sys.stdin.read())
    print(grid)
    for j, line in enumerate(grid):
        for i, pos in enumerate(line):
            if pos==0:
                line = ((x_ticks[i],y_ticks[j]),(x_ticks[i+1],y_ticks[j+1]))
                draw.line(line, fill=28)
            if pos==1:
                line = ((x_ticks[i],y_ticks[j+1]),(x_ticks[i+1],y_ticks[j]))
                draw.line(line, fill=28)
    # 예시
    # point(draw, (0,4))
    # point(draw, (1,3))
    # point(draw, (2,2))
    # point(draw, (3,1))
    # point(draw, (4,0))

    del draw
    f = plt.figure()
    plt.imshow(image)
    plt.axis('off')
    plt.savefig('hihi.png')

    # print(fig2array((f)))
    hi = fig2array((f))#np.asarray(image)
    while True:
        cv2.imshow("test",hi)
        if cv2.waitKey(1) & 0xff == ord('w'):
            break
    cv2.destroyAllWindows()
    # print(hi)
    # plt.show()


# %%
