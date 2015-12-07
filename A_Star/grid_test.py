
class Square:
  def __init__(self):
    self.type = "norm"
    self.move = 0
    self.heur = 0
    self.my_self = None
    self.parent = None
    self.ul = 0
    self.ul_cost = 14
    self.u = 0
    self.u_cost = 10
    self.ur = 0
    self.ur_cost = 14
    self.r = 0
    self.r_cost = 10
    self.br = 0
    self.br_cost = 14
    self.b = 0
    self.b_cost = 10
    self.bl = 0
    self.bl_cost = 14
    self.l = 0
    self.l_cost = 10
#    self.MN = None

  def get_type(self): # get type
    return self.type

  def set_type(self,type): # set type
    self.type = type

  def set_move(self,move):
    self.move = move

  def set_heur(self,heur):
    self.heur = heur

  def set_self(self,my_self):
    self.my_self = my_self

  def set_parent(self,parent):
    self.parent = parent

  # def set_MN(self,MN):
    # self.MN = MN

  # corner setters
  def set_ul(self,ul):
    self.ul = ul
  
  def set_ul_cost(self,ul_cost):
    self.ul_cost = ul_cost
  
  def set_u(self,u):
    self.u = u
  
  def set_ul_cost(self,ul_cost):
    self.ul_cost = ul_cost
  
  def set_ur(self,ur):
    self.ur = ur
  
  def set_ul_cost(self,ul_cost):
    self.ul_cost = ul_cost
  
  def set_r(self,r):
    self.r = r
  
  def set_r_cost(self,r_cost):
    self.r_cost = r_cost
  
  def set_br(self,br):
    self.br = br
  
  def set_br_cost(self,br_cost):
    self.br_cost = br_cost
  
  def set_b(self,b):
    self.b = b
  
  def set_b_cost(self,b_cost):
    self.b_cost = b_cost
  
  def set_bl(self,bl):
    self.bl = bl
  
  def set_bl_cost(self,bl_cost):
    self.bl_cost = bl_cost
  
  def set_l(self,l):
    self.l = l

  def set_l_cost(self,l_cost):
    self.l_cost = l_cost
  
# start getters
  def get_heur(self):
    return self.heur

  def get_self(self):
    return self.my_self

  def get_parent(self):
    return self.parent

  def get_MN(self):
#    print "M =",M," N =",N
    return (M,N)

# corner getters
  def get_ul(self):
    return self.ul
  
  def get_ul_cost(self):
    return self.ul_cost
  
  def get_u(self):
    return self.u
  
  def get_u_cost(self):
    return self.u_cost
  
  def get_ur(self):
    return self.ur
  
  def get_ur_cost(self):
    return self.ur_cost
  
  def get_r(self):
    return self.r
  
  def get_r_cost(self):
    return self.r_cost
  
  def get_br(self):
    return self.br
  
  def get_br_cost(self):
    return self.br_cost
  
  def get_b(self):
    return self.b
  
  def get_b_cost(self):
    return self.b_cost
  
  def get_bl(self):
    return self.bl
  
  def get_bl_cost(self):
    return self.bl_cost
  
  def get_l(self):
    return self.l

  def get_l_cost(self):
    return self.l_cost
  
M = 7 # row 0-6
N = 8 # col 0-7
grid = []

def main():
#  grid = []
#  M = 7 # row 0-6
#  N = 8 # col 0-7



  # fill the grid with normal squares
  for i in range(M): # row
    for j in range(N): # column
      grid.append(Square())

  print len(grid)

  print 3*N+2 # (0:M-1)*N + (0:N-1)
  print grid[3*N+2].get_type()
  print 6*N+7 # M*N-1 = 55

  # set grid MN values
  # for i in range(M):
    # for j in range(N):
      # grid[i*N + j].set_MN((M,N))

  # set grid corner neighbors
  grid[0].set_ul(None)
  print grid[0].get_ul()
  grid[0].set_u(None)
  grid[0].set_ur(None)
  grid[0].set_r((1-1)*N + (2-1))
  grid[0].set_br((2-1)*N + (2-1))
  grid[0].set_b((2-1)*N + (1-1))
  grid[0].set_bl(None)
  grid[0].set_l(None)
  grid[0].set_self(0)
 
  grid[(1-1)*N + (N-1)].set_ur(None)
  print grid[(1-1)*N + (N-1)].get_ur()
  grid[(1-1)*N + (N-1)].set_u(None)
  grid[(1-1)*N + (N-1)].set_ur(None)
  grid[(1-1)*N + (N-1)].set_r((1-1)*N + (2-1))
  grid[(1-1)*N + (N-1)].set_br((2-1)*N + (2-1))
  grid[(1-1)*N + (N-1)].set_b((2-1)*N + (1-1))
  grid[(1-1)*N + (N-1)].set_bl(None)
  grid[(1-1)*N + (N-1)].set_l(None)
  grid[(1-1)*N + (N-1)].set_self((1-1)*N + (N-1))

  grid[(M-1)*N + (N-1)].set_br(None)
  print grid[(M-1)*N + (N-1)].get_br()
  grid[(M-1)*N + (N-1)].set_u(None)
  grid[(M-1)*N + (N-1)].set_ur(None)
  grid[(M-1)*N + (N-1)].set_r((1-1)*N + (2-1))
  grid[(M-1)*N + (N-1)].set_br((2-1)*N + (2-1))
  grid[(M-1)*N + (N-1)].set_b((2-1)*N + (1-1))
  grid[(M-1)*N + (N-1)].set_bl(None)
  grid[(M-1)*N + (N-1)].set_l(None)
  grid[(M-1)*N + (N-1)].set_self((M-1)*N + (N-1))

  grid[(M-1)*N + (1-1)].set_bl(None)
  print grid[(M-1)*N + (1-1)].get_bl()
  grid[(M-1)*N + (1-1)].set_u(None)
  grid[(M-1)*N + (1-1)].set_ur(None)
  grid[(M-1)*N + (1-1)].set_r((1-1)*N + (2-1))
  grid[(M-1)*N + (1-1)].set_br((2-1)*N + (2-1))
  grid[(M-1)*N + (1-1)].set_b((2-1)*N + (1-1))
  grid[(M-1)*N + (1-1)].set_bl(None)
  grid[(M-1)*N + (1-1)].set_l(None)
  grid[(M-1)*N + (1-1)].set_self((M-1)*N + (1-1))
# end of corner setup

# top middle: row = 0, col = 1:N-2
  for i in range(1,N-2):
    grid[i].set_ul(None)
    grid[i].set_u(None)
    grid[i].set_ur(None)
    grid[i].set_r(i+1)
    grid[i].set_br(N+i+1)
    grid[i].set_b(N+i)
    grid[i].set_bl(N+i-1)
    grid[i].set_l(i-1)
    grid[i].set_self(i)
# end of top middle

# right middle: row = 1:M-2, col = N-1
#(1-(M-2))*N + (N-1)
  for i in range(1,M-2):
    grid[M*i+(N-1)].set_ul(M*(i-1)+(N-2))
    grid[M*i+(N-1)].set_u(M*(i-1)+(N-2))
    grid[M*i+(N-1)].set_ur(None)
    grid[M*i+(N-1)].set_r(None)
    grid[M*i+(N-1)].set_br(None)
    grid[M*i+(N-1)].set_b(M*(i+1)+(N-2))
    grid[M*i+(N-1)].set_bl(M*(i+1)+(N-2))
    grid[M*i+(N-1)].set_l(M*i+(N-2))
    grid[M*i+(N-1)].set_self(M*i+(N-1))
# end of right middle

# bottom middle: row = M-1, col = 1:N-2
#(M-1)*N + (1-(N-2))
  for i in range(1,N-2):
    grid[(M-1)*N+i].set_ul((M-2)*N+i-1)
    grid[(M-1)*N+i].set_u((M-2)*N+i)
    grid[(M-1)*N+i].set_ur((M-2)*N+i+1)
    grid[(M-1)*N+i].set_r((M-1)*N+i+1)
    grid[(M-1)*N+i].set_br(None)
    grid[(M-1)*N+i].set_b(None)
    grid[(M-1)*N+i].set_bl(None)
    grid[(M-1)*N+i].set_l((M-1)*N+i-1)
    grid[(M-1)*N+i].set_self((M-1)*N+i)
# end of bottom middle
  print "Fill left middle"
# left middle: row = 1:M-2, col = 0
#(1-(M-2))*N + (1-1)
  for i in range(1,M-1):
    grid[i*N].set_ul(None)
    grid[i*N].set_u((i-1)*N)
    grid[i*N].set_ur((i-1)*N+1)
    grid[i*N].set_r(i*N+1)
    grid[i*N].set_br((i+1)*N+1)
    grid[i*N].set_b((i+1)*N)
    grid[i*N].set_bl(None)
    grid[i*N].set_l(None)
    grid[i*N].set_self(i*N)
# end of left middle
  print "Test left middle"
# Now do some testing
# left middle: row = 1:M-2, col = 0
#(1-(M-2))*N + (1-1)
  for i in range(1,M-1):
    print grid[i*N].get_ul()
    print grid[i*N].get_u()
    print grid[i*N].get_ur()
    print grid[i*N].get_r()
    print grid[i*N].get_br()
    print grid[i*N].get_b()
    print grid[i*N].get_bl()
    print grid[i*N].get_l()
    print grid[i*N].get_self()
    print
# end of left middle

# inner squares: row = 1:M-2, col = 1:N-2
#(1-(M-2))*N + (1-(N-2))
  for i in range(1,M-1):
    for j in range(1,N-1):
      grid[i*N + j].set_ul((i-1)*N+(j-1))
      grid[i*N + j].set_u((i-1)*N+(j))
      grid[i*N + j].set_ur((i-1)*N+(j+1))
      grid[i*N + j].set_r((i)*N+(j+1))
      grid[i*N + j].set_br((i+1)*N+(j+1))
      grid[i*N + j].set_b((i+1)*N+(j))
      grid[i*N + j].set_bl((i+1)*N+(j-1))
      grid[i*N + j].set_l((i)*N+(j-1))
      grid[i*N + j].set_self(i*N + j)
# end of inner squares
  print "Test left middle"
# Now do some testing
# left middle: row = 1:M-2, col = 0
#(1-(M-2))*N + (1-1)
  for i in range(1,M-1):
    print grid[i*N].get_ul()
    print grid[i*N].get_u()
    print grid[i*N].get_ur()
    print grid[i*N].get_r()
    print grid[i*N].get_br()
    print grid[i*N].get_b()
    print grid[i*N].get_bl()
    print grid[i*N].get_l()
    print grid[i*N].get_self()
    print
# end of left middle

  print "end of grid_test"
















  """
  grid.append(Square())
  grid.append(Square())

  print grid
  print grid[0].get_type()
  grid[0].set_type("src")
  print grid[0].get_type()
  grid[1].set_type("dest")
  print grid[1].get_type()
  """
if __name__ == '__main__':
  main()









