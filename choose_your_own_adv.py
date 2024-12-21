print(r'''
 _.-'`"=-+`";.
                                                                        _.- `   _/ :.
                                                                  -'`         .=+"'*+._ 
                                                                           .;":``     `""+=.
                                                                      __.+'::`             "+
                                                                 _.+`"   `'::.-+`            ".
                                                            .--+"`        .:"  `"+            +.
                               '.   _.---.            __.+`"`.          .:^     `";;+'       ":;
         .--'` `                  `"`*+.   \:`'"+._.n:"    '`____. ,.  ' /   __    +.+'        ;:
  _ _.-'`                     `-+'+::+~`'"`"-:`-+:.   ___.--`_+;;+?`     ; '`  ` /".=.:.      f:
                                              `"` `":.___.--`;. ..`     /  ,.-  ..:/  ;:`     .:
                                                             :: :`     /      .=`:/) /      .:;"
                             .--.                            `. ;      -,      .'"`           ;
                           .:_.--+-.          ` --._____       `;:.     '_        ,m   .-"  .;`
               ___    _.--'.--"` '.  .            _.+"` _"`-.    ;       "'     _+dMM:` /  .;`\
        .--'`    `'"-.,__.--.      : :          .' ._+"`     "-.."-.     ;  _.`"."P" _.- .:`. "*+._
      .'                     +_.-:/  /          :`.+`       .---:`"-._    `'   .-"     ./ .:`.:   `:;
     /                       __ _:  ;           ';`-.     .'       _.-`"`+---,-`    _.-"/:.      .::+"
                      .--'`'`  `-._'.\          __+.___.--:__  .-`         _.-+  "`-._.-m::  /  ':.\
                 __.-` __.-`"        `+-._.-+""`--"               _.' _.cmf`        `+::"_.+; .:::+"
              .-"` --"`       .                               ."`    _dM"YMMb          \  `"m.:::.
            /` .-^- --+. ``'-._'.                        .--/   _.mfMMNb.`"WI.             .'M / /  
         .-``./        `;.     _.'.-.               _.-`__.`_.-``"*+m YMb.`MMI.       ;`"   I`-.
        /              ."_ __.'<'   `-.   ___. --'`_.=+` .-`       `Yb MMb: lM:             d'  ;
                  _.-'    .'   '.`.     `"'--====="`  .-'           `+Y,"Mb.YMM. _.-`        d  -'
             .-"`       .+_    .' ;             /  .-`                f+YMmf+*"""`          i" 
 .-"`-.     /       _.-'.-'`-./_.'             +-           .      .`**"`*"`             .i"
       )    .-"` `""-.____.-"`              .-'          _."  _.-'                   _.m"`
       '._.'                             .-"b.          ."-+="`                   ,m+"`
                                    _.i::  `".       _.-"` /                  .d"`
                                 _.dW;:YWb.   '-. .-`:    ;                d"`
                               .' `"YM;:YWWm. _.    /    .b.            :I"
                             .'     `WWn:WP*"`|    ;    pI Am._       .mMM._.
                            :      .-`"*"     :        :MA."WWMbm+._.iMmMMMM:
                            :    .:/         .dSSSSb  .:MMMm.`**YMMMM.dMMMMMMf ._
                           _;   ` '          `:`   \ `*'WMMMMAm.."YY".mMMmdMMMmMMP"
                          / `                 \     ; `fMMMMMMMMMmMMMMSMMMMMM+"Ym
                       .-;   __.'              ;    `  .mSSs.WMMMMSMSMSMmMMMMM*\ "`
                       _<+ .+                 /   .`  dRSSSP"*+FMMMMMMMFf*MMP`  :
                        ."-/                 ,   +__.dRRSSP ;    `'"""`'""       `
                                    ._ ,_-`'-ssSRRRRPmSSP` /      .'
                                   . ,`' `'.::.`"+SSRRRP".:         _.`  /        |
                                   ::'  _`  `;:::..,.,.;:;`     _.-'__.-`         ;
                                  `;,:;`  ,           .' :  _.-``"`       
                                    -:;-`.;:.  ,-:,:::/  /-`              /       .
                                       ':/`-;` `" `;:/  ;:::`       __..-'       /
                                      _.'         .-'   :::`    _.-'           .;
                                   .-'         .-'      ;:` .-"`           _.="|
                                .-'.    .-'_.'`         ::.'`            .="`` ;      zi.
                             .-'.-'    /s;Y"`           ;/           .="`      `
                       _ -="`         /S"`              /        .-"`           .
                   `"- ---=;`>;.  ;  ;P`               ;       /"`
                     `"'--_;->;:'   ./`                        :    
                    ---._ -~_;;;.:./"`                          '  
             .----._-.__.`"'`:;;;;"                   
                    `"'"-._-"";;-`  
                         _.-`"
                         
''')
print("Welcome to the game.")
print("Your mission is to find a way to meet the woman.")

left_or_right = input("You find yourself on a forest trail. There are two paths; left and right. On the left path, you can faintly hear what sounds like a young woman singing. On the right path, you smell the odor of BBQ. Which path are you taking? Left or right?: ")
if left_or_right == "Left" or left_or_right == "left":
    print("You find a stumble across a winding river with a strong current. On the other side of the river, a woman is sitting on a rock singing a heavenly tune.")
    swim_or_wait = input("Will you swim across the river to introduce yourself or wait for an opportunity?: ")

    if swim_or_wait == "Wait" or swim_or_wait == "wait":
        print("After some time, the woman noticed you and smiled. She raised her hands in the air and three different colored magical doors appear in front of you.")
        color_door = input("Which color door will you pick? Red, blue or yellow?: ")

        if color_door == "Red" or color_door == "red":
            print("When you opened the red door, several tortured souls pulled you into hell and you are burned alive by fire. Game over.")
        elif color_door == "Blue" or color_door == "blue":
            print("Before you could open the blue door, 5 fierce wolves burst through the door and you were eaten alive by blood-thirsty beasts. Game over.")
        elif color_door == "Yellow" or color_door == "yellow":
            print("The yellow door was a clear option as it symbolized the woman's heavenly looks and voice. When opened and stepped through, you are teleported to the woman. She tells you that you passed the test and are granted one wish. You've won.")
        else:
            print("Game over.")

    else:
        print("You tried to swim in the river, but the current was too strong and thrashed your body against multiple rocks. The woman noticed you and shrieked for help, but you drowned before anyone came to your rescue. Game over.")

else:
    print("Led by the smell of BBQ, you find that there was no barbeque to be found. You are met by raiders and they rob you. Game over.")





