import pygame as pg

import platform


# fonction qui gère le menu principal
def menu(screen, win_w, win_h, font):
	logo = pg.image.load("logo.png")
	p1 = pg.image.load("p1.png")
	p2 = pg.image.load("p2.png")

	jouerTxt = font.render("vs IA", False, (255, 255, 255))
	joueursTxt = font.render("vs J2", False, (255, 255, 255))
	quitterTxt = font.render("Quitter", False, (255,255,255))

	if platform.system() == "Linux":
		rect = pg.Rect(win_w * 0.39, win_h * 0.5, win_w * 0.19, win_h * 0.15)
		rect1 = pg.Rect(win_w * 0.39, win_h * 0.65, win_w * 0.19, win_h * 0.15)
		rect2 = pg.Rect(win_w * 0.39, win_h * 0.8, win_w * 0.19, win_h * 0.15)
	else:
		rect = pg.Rect(win_w * 0.41, win_h * 0.53, win_w * 0.19, win_h * 0.15)
		rect1 = pg.Rect(win_w * 0.41, win_h * 0.68, win_w * 0.19, win_h * 0.15)
		rect2 = pg.Rect(win_w * 0.41, win_h * 0.83, win_w * 0.19, win_h * 0.15)

	selected = 0

	temps = pg.time.get_ticks()

	continuer = True

	while continuer:

		if temps + 75 <= pg.time.get_ticks():
			temps = pg.time.get_ticks()

			event = pg.key.get_pressed()

			if event[pg.K_UP] or event[pg.K_z]:
				if selected == 1:
					selected = 0
				elif selected == 2:
					selected = 1
			elif event[pg.K_DOWN] or event[pg.K_s]:
				if selected == 0:
					selected = 1
				elif selected == 1:
					selected = 2

			elif event[pg.K_RETURN] or event[pg.K_KP_ENTER]:
				continuer = False

		# Pour quitter la fenetre
		for events in pg.event.get():
			if events.type == pg.QUIT:
				exit()

		screen.fill(0)

		if selected == 0:
			pg.draw.rect(screen, pg.Color(255,255,255), rect, 3)
		elif selected == 1:
			pg.draw.rect(screen, pg.Color(255,255,255), rect1, 3)
			screen.blit(p2, (win_w * 0.8, win_h * 0.4))
		else:
			pg.draw.rect(screen, pg.Color(255,255,255), rect2, 3)

		screen.blit(logo, (win_w * 0.4, win_h * 0.1))
		screen.blit(p1, (win_w * 0.1, win_h * 0.4))
		screen.blit(jouerTxt, (win_w * 0.45, win_h * 0.55))
		screen.blit(joueursTxt, (win_w * 0.45, win_h * 0.7))
		screen.blit(quitterTxt, (win_w * 0.43, win_h * 0.85))

		pg.display.flip()

	if selected == 2:
		exit()
	elif selected == 0:
		return True
	else:
		return False