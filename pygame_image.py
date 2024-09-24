import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#練習１
    bg1_img = pg.transform.flip(bg_img, True, False) #練習７
    kk_img = pg.image.load("fig/3.png") #練習２
    kk_img = pg.transform.flip(kk_img, True, False) #練習２
    kk_rct = kk_img.get_rect()#練習８ー１：surfaceからrectを抽出する
    kk_rct.center = 300, 200#練習８－２：rectを使った初期座標の設定 

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_list = pg.key.get_pressed() #練習８－３：キーの降下状態を取得
        if key_list[pg.K_UP]:#上矢印キーがTrueなら
            kk_rct.move_ip((0, -1))
        if key_list[pg.K_DOWN]:#下矢印キーがTrueなら
            kk_rct.move_ip((0, +1))
        if key_list[pg.K_LEFT]:#左矢印キーがTrueなら
            kk_rct.move_ip((-1, 0))
        if key_list[pg.K_RIGHT]:#右矢印キーがTrueなら
            kk_rct.move_ip((+1, 0))
        
        x = -(tmr%3200) #練習６
        screen.blit(bg_img, [x, 0])#練習３
        screen.blit(bg1_img, [x+1600, 0])#練習７
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg1_img, [x+4800, 0])
        screen.blit(kk_img, kk_rct) #練習４
        pg.display.update()
        tmr += 1        
        clock.tick(400) #練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()