import pygame as pg



def menu(screen, win_w, win_h, font):
	logo = pg.image.load("logo.png")

	jouerTxt = font.render("Jouer", False, (255, 255, 255))

	quitterTxt = font.render("Quitter", False, (255,255,255))

	rect = pg.Rect(win_w * 0.42, win_h * 0.5, win_w * 0.16, win_h * 0.15)
	rect2 = pg.Rect(win_w * 0.42, win_h * 0.7, win_w * 0.16, win_h * 0.15)

	selected = 0

	continuer = True

	while continuer:
		event = pg.key.get_pressed()

		if event[pg.K_UP] and selected == 1:
			selected = 0
		elif event[pg.K_DOWN] and selected == 0:
			selected = 1
		elif event[pg.K_RETURN] or event[pg.K_KP_ENTER]:
			continuer = False

		# Pour quitter la fenetre
		if event[pg.K_ESCAPE]:
			continuer = False
		for events in pg.event.get():
			if events.type == pg.QUIT:
				exit()

		screen.fill(0)

		if selected == 0:
			pg.draw.rect(screen, pg.Color(255,255,255), rect, 3)
		else:
			pg.draw.rect(screen, pg.Color(255,255,255), rect2, 3)
		screen.blit(logo, (win_w * 0.4, win_h * 0.1))
		screen.blit(jouerTxt, (win_w * 0.46, win_h * 0.55))
		screen.blit(quitterTxt, (win_w * 0.45, win_h * 0.75))

		pg.display.flip()

	if selected == 1:
		exit()
	else:
		return True