# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/28 5:18 下午
@Auth ： Codewyf
@File ：p18_1.py.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

import pygame
import sys

pygame.init()

size = width, height = 600, 400
speed = [-2,1]
bg = (255,255,255)

#create window
screen = pygame.display.set_mode(size)

#set window name
pygame.display.set_caption('初次见面，请大家多多关照!')
turtle = pygame.image.load("turtle.png")
#get the pic position
position = turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#move the pic
position = position.move(speed)
if position.left < 0 or position.right >width:
    #反转图像
    turtle = pygame.transform.flip(turtle, True, False)
    #反方向移动
    speed[0] = -speed[0]

if position.top < 0 or position.bottom > height:
    speed[1] = -speed[1]

screen.fill(bg)
screen.blit(turtle, position)
pygame.display.flip()
#pygame.display.update()
pygame.time.delay(10)