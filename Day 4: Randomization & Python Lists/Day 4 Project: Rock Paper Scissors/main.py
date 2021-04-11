import random
welcome = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░
"""

logo = """
                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                     
RRRRRRRRRRRRRRRRR                                        kkkkkkkk                PPPPPPPPPPPPPPPPP                                                                                                         &&&&&&&&&&            SSSSSSSSSSSSSSS                       iiii                                                                                          
R::::::::::::::::R                                       k::::::k                P::::::::::::::::P                                                                                                       &::::::::::&         SS:::::::::::::::S                     i::::i                                                                                         
R::::::RRRRRR:::::R                                      k::::::k                P::::::PPPPPP:::::P                                                                                                     &::::&&&:::::&       S:::::SSSSSS::::::S                      iiii                                                                                          
RR:::::R     R:::::R                                     k::::::k                PP:::::P     P:::::P                                                                                                   &::::&   &::::&       S:::::S     SSSSSSS                                                                                                                    
  R::::R     R:::::R   ooooooooooo       cccccccccccccccc k:::::k    kkkkkkk       P::::P     P:::::Paaaaaaaaaaaaa  ppppp   ppppppppp       eeeeeeeeeeee    rrrrr   rrrrrrrrr       ssssssssss          &::::&   &::::&       S:::::S                cccccccccccccccciiiiiii     ssssssssss       ssssssssss      ooooooooooo   rrrrr   rrrrrrrrr       ssssssssss   
  R::::R     R:::::R oo:::::::::::oo   cc:::::::::::::::c k:::::k   k:::::k        P::::P     P:::::Pa::::::::::::a p::::ppp:::::::::p    ee::::::::::::ee  r::::rrr:::::::::r    ss::::::::::s          &::::&&&::::&        S:::::S              cc:::::::::::::::ci:::::i   ss::::::::::s    ss::::::::::s   oo:::::::::::oo r::::rrr:::::::::r    ss::::::::::s  
  R::::RRRRRR:::::R o:::::::::::::::o c:::::::::::::::::c k:::::k  k:::::k         P::::PPPPPP:::::P aaaaaaaaa:::::ap:::::::::::::::::p  e::::::eeeee:::::eer:::::::::::::::::r ss:::::::::::::s         &::::::::::&          S::::SSSS          c:::::::::::::::::c i::::i ss:::::::::::::s ss:::::::::::::s o:::::::::::::::or:::::::::::::::::r ss:::::::::::::s 
  R:::::::::::::RR  o:::::ooooo:::::oc:::::::cccccc:::::c k:::::k k:::::k          P:::::::::::::PP           a::::app::::::ppppp::::::pe::::::e     e:::::err::::::rrrrr::::::rs::::::ssss:::::s         &:::::::&&            SS::::::SSSSS    c:::::::cccccc:::::c i::::i s::::::ssss:::::ss::::::ssss:::::so:::::ooooo:::::orr::::::rrrrr::::::rs::::::ssss:::::s
  R::::RRRRRR:::::R o::::o     o::::oc::::::c     ccccccc k::::::k:::::k           P::::PPPPPPPPP      aaaaaaa:::::a p:::::p     p:::::pe:::::::eeeee::::::e r:::::r     r:::::r s:::::s  ssssss        &::::::::&   &&&&         SSS::::::::SS  c::::::c     ccccccc i::::i  s:::::s  ssssss  s:::::s  ssssss o::::o     o::::o r:::::r     r:::::r s:::::s  ssssss 
  R::::R     R:::::Ro::::o     o::::oc:::::c              k:::::::::::k            P::::P            aa::::::::::::a p:::::p     p:::::pe:::::::::::::::::e  r:::::r     rrrrrrr   s::::::s            &:::::&&::&  &:::&            SSSSSS::::S c:::::c              i::::i    s::::::s         s::::::s      o::::o     o::::o r:::::r     rrrrrrr   s::::::s      
  R::::R     R:::::Ro::::o     o::::oc:::::c              k:::::::::::k            P::::P           a::::aaaa::::::a p:::::p     p:::::pe::::::eeeeeeeeeee   r:::::r                  s::::::s        &:::::&  &::&&:::&&                 S:::::Sc:::::c              i::::i       s::::::s         s::::::s   o::::o     o::::o r:::::r                  s::::::s   
  R::::R     R:::::Ro::::o     o::::oc::::::c     ccccccc k::::::k:::::k           P::::P          a::::a    a:::::a p:::::p    p::::::pe:::::::e            r:::::r            ssssss   s:::::s      &:::::&   &:::::&                   S:::::Sc::::::c     ccccccc i::::i ssssss   s:::::s ssssss   s:::::s o::::o     o::::o r:::::r            ssssss   s:::::s 
RR:::::R     R:::::Ro:::::ooooo:::::oc:::::::cccccc:::::ck::::::k k:::::k        PP::::::PP        a::::a    a:::::a p:::::ppppp:::::::pe::::::::e           r:::::r            s:::::ssss::::::s     &:::::&    &::::&       SSSSSSS     S:::::Sc:::::::cccccc:::::ci::::::is:::::ssss::::::ss:::::ssss::::::so:::::ooooo:::::o r:::::r            s:::::ssss::::::s
R::::::R     R:::::Ro:::::::::::::::o c:::::::::::::::::ck::::::k  k:::::k       P::::::::P        a:::::aaaa::::::a p::::::::::::::::p  e::::::::eeeeeeee   r:::::r            s::::::::::::::s      &::::::&&&&::::::&&     S::::::SSSSSS:::::S c:::::::::::::::::ci::::::is::::::::::::::s s::::::::::::::s o:::::::::::::::o r:::::r            s::::::::::::::s 
R::::::R     R:::::R oo:::::::::::oo   cc:::::::::::::::ck::::::k   k:::::k      P::::::::P         a::::::::::aa:::ap::::::::::::::pp    ee:::::::::::::e   r:::::r             s:::::::::::ss        &&::::::::&&&::::&     S:::::::::::::::SS   cc:::::::::::::::ci::::::i s:::::::::::ss   s:::::::::::ss   oo:::::::::::oo  r:::::r             s:::::::::::ss  
RRRRRRRR     RRRRRRR   ooooooooooo       cccccccccccccccckkkkkkkk    kkkkkkk     PPPPPPPPPP          aaaaaaaaaa  aaaap::::::pppppppp        eeeeeeeeeeeeee   rrrrrrr              sssssssssss            &&&&&&&&   &&&&&      SSSSSSSSSSSSSSS       cccccccccccccccciiiiiiii  sssssssssss      sssssssssss       ooooooooooo    rrrrrrr              sssssssssss    
                                                                                                                     p:::::p                                                                                                                                                                                                                                         
                                                                                                                     p:::::p                                                                                                                                                                                                                                         
                                                                                                                    p:::::::p                                                                                                                                                                                                                                        
                                                                                                                    p:::::::p                                                                                                                                                                                                                                        
                                                                                                                    p:::::::p                                                                                                                                                                                                                                        
                                                                                                                    ppppppppp                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                     
"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(welcome)
print(logo)
game_images = [rock, paper, scissors]

print(rock, "Type 0 for Rock")
print(paper, "Type 1 for Paper")
print(scissors, "Type 2 for Scissors")

user_choice = int(input("\n What do you choose? \n"))
