#Objectives#
In this lab, you will:
* Practice collision detection and response
* Practice using Git and GitHub
* Be exposed to reading and using other people's work
* Hack Pong

#Overview#
I have provided `pong.py`.  Run the program via `python pong.py`
(Pygame required).  Move the paddle with either the UP or DOWN arrow
keys or use the mouse.  If your paddle hits the ball, you score a
point.  The problem is: this isn't Pong as you know it.  Enough said.

#Instructions#
* (1 point) There is only one score --for you.  Add another score on
  the display for the opponent.  Your score shall be displayed at the
  top middle half of the left side of the board while the opponent's
  score shall be displayed at the top middle half of the right side of
  the board.

* (1 point) As of right now, if you miss the ball (that is, the ball
  hits your wall on the left), it bounces.  Change the source code so
  that if the ball hits your wall, the opponent scores a point.

* (1 point) Change the source code so that instead of receiving a
  point if your paddle hits the ball, you receive a point only if the
  ball hits the right wall.

* (1 point) When the ball collides with a paddle, play a sound (find
  one).

* (1 point) Implement a second paddle on the right side. :-) Duh!

* (1 point) Draw a line (e.g., a dotted black line, a solid red line)
  dividing the playing surface, as in the real game of Pong.

* (1 point) Change the source so if the ball hits a wall (i.e.,
  someone scores), reset the ball to the middle of the playing surface
  and move the ball to the player who got scored on.

* (1 point) Change the source so if a player scores 11 points, the
  game is over.  That is, display who wins and prompt for a rematch.
  If rematch, reset the scores to 0 - 0.

* Either: (1 point) change your paddle to move using the "W" (up) and
"S" (down) keys and use the UP and DOWN arrows for the opponent
paddle, OR (1 point + 1 bonus point) make the opponent paddle play on
its own. But don't make the opponent impossibly hard!

* (1 point) Push your work to your GitHub account.

#Submission#
Push your work to your GitHub account and **send me a message (to
mchow01) via Notifications in GitHub.** Notifications is under the
radio waves icon to the right of your GitHub username (and to the
right of the Account Settings and Log Out icons) at the top navigation
bar. **I will not accept emails!***

#Notes
* You are encouraged to commit and push as many times as you want.
* Please do not "wing" your commit messages, they should be readable. 
