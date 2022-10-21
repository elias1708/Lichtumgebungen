# -*- coding: utf-8 -*-
"""
Die Analyse der Auswirkungen von verschiedenen Lichtfarben und Helligkeitsstufen /
auf die Leseverständnis- und die Gedächtnisfähigkeiten von Lernenden.

Elias Vo Thanh

"""

from tkinter import *
from PIL import Image, ImageTk
import time
import csv


##################################################
################### FIRST GAME ###################
##################################################

def game1():
    """
    opens first game window.
    
    """

    # open first window for game
    window1 = Tk()
    window1.title("Anleitung Spiel 1")
    

     
    inputbox = Entry(window1, bd = 5, width = 40)
    game1_label = Label(window1, text = "Lies den Text und wähle die richtige Lösung aus.\n \
    Es gibt immer nur eine richtige Antwort. \n \
    Bewertet wird die richtige Lösung und die benötigte Zeit. \n \n \
    Bitte gib hier deinen Namen ein und bestätige.")

    # Solution of participant of each task of game 1
    radioValue = IntVar(window1)
    radioValue1 = IntVar(window1)
    radioValue2 = IntVar(window1)
    radioValue3 = IntVar(window1)

    window1.geometry('900x900')

    def press4(t_start7):
        """
        Write solution and time in csv file. End the first game.

        Input: t_start7 is the starting time
        """

        # to measure time
        t_end5 = time.time() - t_start7

        # get solution
        story_entry = radioValue3.get()
        
        # write into csv file
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end5])


        # open new window for next task
        window15 = Tk()
        window15.title("EndeSpiel1")
        window15.geometry('600x200')

    def press3(t_start6):
        """
        Displays task and options.

        Input: t_start6 is the starting time
        """

        # to measure time
        t_end4 = time.time() - t_start6

        game1_label.config(text='Eine Hausfrau erzählt:\n \n \
        Also am Sonntag bin ich mal wieder explodiert. Das kam so: Ich hatte am Samstag\n \
        die Wohnung saubergemacht. Aber als ich am Sonntag als erste aufstand und ins\n \
        Wohnzimmer kam, da hatte ich genug! - Da lag sein Bademantel, da standen seine\n \
        Hausschuhe, die Zigarrenasche überall verteilt. Ich machte die Badezimmertür auf:\n \
        Das Handtuch in der Badewanne, die Unterwäsche meiner Töchter daneben.\n \
        Auf der Treppe stolperte ich über Fußballschuhe. Das war um neun. Um zehn\n \
        haben wir gefrühstückt. Um elf war ich wieder mutterseelenallein.\n \
        Ich hatte noch kein Mittagessen gekocht, und das Haus sah aus wie ein Trümmmerhaufen.\n \
        Meine beiden Töchter hatten sich ins Kinderzimmer zurückgezogen, um Schallplatten zu hören.\n \
        Die Jungen waren Fußballspielen gegangen, und mein Mann musste zu Bekannten, die ein Baby\n \
        bekommen hatten. Da habe ich angefangen zu heulen. Ich hätte ja sagen können: Ich lass den\n \
        ganzen Dreck liegen, aber das Essen musste auf den Tisch, und nachmittags kam Besuch.\n \
        Nach einer Weile erschienen meine Töchter, guckten mich an und sagten: "Mama was hast du, ist dir nicht gut?"\n \
        Natürlich tat ich ihnen leid, und sie halfen mir, so gut sie konnten.\n \
        Ich sagte: "Ich weiß, dass ihr mir helft, wenn ich euch darum bitte. Aber ist es euch schon\n \
        aufgefallen, dass immer nur wir sonntags arbeiten? Die Herren machen sich aus dem Staub, und\n \
        wir müssen schuften."\n \
        Zum Essen waren alle wieder da. Mein Mann hatte vier Cognacs getrunken und war bester Laune.\n \
        Die Jungen sahen aus wie die Schweine. Und ich habe nur geweint:\n \
        "Was denkt ihr eigentlich, was ich bin? Ich habe keinen Sonnabend, ich habe keinen Sonntag,\n \
        fällt euch das nicht auf?" "Mein Gott", sagte mein Mann, "du hättest doch einen Ton sagen können."\n \
        - "Wieso," fragte ich, "hätte ich einen Ton sagen müssen? Du hast doch Augen im Kopf.\n \
        Hast du nicht gesehen, dass du alles liegengelassen hast?" Na ja, und dann bin ich gegangen.\n \
        Da haben die Männer das Geschirr gespült und versprochen, dass ab nächsten Sonntag alles anders werden soll.\n \
        Abends hat mich mein Mann in das französische Restaurant eingeladen, wo ich so gerne hingehe,\n \
        und mir auch einen Hunderter in die Hand gedrückt. Er hat gemerkt, dass ich in diesem Monat ein\n \
        bisschen knapp mit dem Haushaltsgeld bin, weil zwei unserer Kinder Geburtstag haben.\n \n \
        Welche ist die einzige wahre Aussage? Klicke die richtige Aussage an und bestätige.\n')

        # different solution options
        option1 = Radiobutton(window1,text="a) Der Vater ist früher aufgestanden.",
                                     variable=radioValue3, value=1)
        option1.pack()

        option2 = Radiobutton(window1,text="b) Die Frau weinte, weil der Mann betrunken war.",
                                     variable=radioValue3, value=2)
        option2.pack()
        
        option3 = Radiobutton(window1,text="c) Der Mann besuchte nach dem Früchstück einen Bekannten.",
                                     variable=radioValue3, value=3)
        option3.pack()
        
        option4 = Radiobutton(window1,text="d) Die Mutter hat am Vormittag allein die Arbeit im Haushalt gemacht.",
                                     variable=radioValue3, value=4)
        option4.pack()
        
        option5 = Radiobutton(window1,text="e) Die Kleidungsstücke der Tochter lagen auf der Treppe.",
                                     variable=radioValue3, value=5)
        option5.pack()

        # to measure time
        t_start7 = time.time()
        
        # destroy all options and pass time value
        next1_button['command'] = lambda: [press4(t_start7), option1.destroy(), 
                                           option2.destroy(), option3.destroy(), 
                                           option4.destroy(), option5.destroy(), 
                                           window1.destroy()]
        
        next1_button.config(text="Eingabe bestätigen")   
        
        window1.title("Spiel1.4")
        
    def press19(t_start5):
        """
        Write solution and time in csv file.

        Input: t_start7 is the starting time
        """
        # to measure time
        t_end3 = time.time() - t_start5
        
        # get solution
        story_entry = radioValue2.get() 
        
        # write into csv file
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end3])

        # to measure time
        t_start6 = time.time()

        game1_label.config(text="Weiter zu Spiel 1.4.")        

        
        next1_button.config(text="Bestätigen.")



        next1_button['command'] = lambda: press3(t_start6)
        
    def press2(t_start4):
        """
        Displays task and options.

        Input: t_start4 is the starting time
        """
        game1_label.config(text='Ferien auf dem Bauernhof\n \n \
        Ferien auf dem Bauernhof, das gibt es mindestens schon seit zwanzig Jahren.\n \
        Vor allem bei Familien mit kleineren Kindern und bei älteren Leuten sind sie sehr beliebt,\n \
        weniger dagegen bei Jugendlichen. Im letzten Jahr verbrachten mehr als 600.000 Deutsche ihre\n \
        Ferien auf dem Lande; fast die Hälfte davon waren Kinder. Und die meisten von ihnen waren sehr\n \
        zufrieden, wie Reporter einer großen Tageszeitung herausfanden.\n \
        Vor allem gefielen diesen Feriengästen die freundliche Atmosphäre, die Ruhe, die Schönheit der\n \
        Landschaft und nicht zuletzt das gute Essen. Natürlich spielt auch der Preis eine Rolle.\n \
        Eine Familie mit zwei Kindern gibt im Durchschnitt für einen vierzehntägigen Aufenhalt auf\n \
        einem Bauernhof etwa 800 Euro aus. Das ist, verglichen mit anderen Urlaubsangeboten, nicht teuer.\n \
        Die meisten Gäste wünschen sich einen Bauernhof, der noch in Betrieb ist; und es ist besonders\n \
        wichtig, dass Tiere da sind. Zu einem richtigen Bauernhof gehören eben Hühner und Gänse,\n \
        Schweine und Pferde und außerdem natürlich Kühe, damit die Kinder lernen, wo die Milch herkommt.\n \
        Fast alle Gäste kommen nämlich aus Großstädten. Und Hunde und Katzen dürfen als Spielgefährten\n \
        für die Kinder ebenfalls nicht fehlen. Sehr oft sind es denn auch die Kinder, die den Vorschlag\n \
        machen, die Ferien einmal auf einem Bauernhof zu verbringen. Ungefähr 20.000 landwirtschaftliche\n \
        Betriebe bieten in diesem Jahr in der Bundesrepublik Deutschland Betten für Feriengäste an.\n \
        Die Zahl nimmt noch zu, denn die wirtschaftliche Lage auf dem Lande ist sehr schwierig geworden.\n \
        Viele Landwirte hätten ohne das Geschäft mit dem Tourismus die Landwirtschaft längst aufgeben müssen.\n \
        Einige Landwirte verdienen durch den Tourismus so gut, dass sie es nicht mehr nötig haben, ihre\n \
        Felder zu bearbeiten. Sie sind dann auch gerne bereit, ihr Land zu verkaufen. Manchmal will man\n \
        darauf Golfplätze, Häuser, Supermärkte oder sogar Fabriken bauen. Doch solche Pläne stoßen heute\n \
        meistens auf den Widerstand der Naturschützer. Sie kämpfen dafür, dass es in Deutschland wieder mehr\n \
        Gebiete gibt, wo Pflanzen und Tiere in natürlicher Umgebung ungestört wachsen und leben können.\n \
        Auf einigen Bauernhöfen oder in ihrer Nähe werden auch Sportmöglichkeiten angeboten, vor allem Reiten,\n \
        Tennis oder Schwimmen. Aber die meisten Gäste ziehen es vor, sich auszuruhen und sich zu erholen.\n \
        Einige möchten auf dem Bauernhof mitarbeiten, doch das haben die Landwirte im allgemeinen nicht so gern,\n \
        denn dabei sind schon zu viele Unfälle geschehen. Und wie erfährt man, auf welchen Bauernhöfen man\n \
        Ferien machen kann? Man kann sich natürlich bei einem Reisebüro informieren, aber die meisten\n \
        Feriengäste haben durch Freunde oder Bekannte eine gute Adresse bekommen.\n \n \
        Welche ist die einzige wahre Aussage? Klicke die richtige Aussage an und bestätige.\n')
        
        # different solution options
        option1 = Radiobutton(window1,text="a) Die meisten Feriengäste kommen aus der näheren Umgebung.",
                                     variable=radioValue2, value=1) 
        option1.pack()
        
        option2 = Radiobutton(window1,text="b) Kinder bezahlen nur die Hälfte.",
                                     variable=radioValue2, value=2) 
        option2.pack()
        
        option3 = Radiobutton(window1,text="c) Auf allen Bauernhöfen werden Sportmöglichkeiten angeboten.",
                                     variable=radioValue2, value=3) 
        option3.pack()
        
        option4 = Radiobutton(window1,text="d) Die Gäste sollen auf dem Bauernhof nicht helfen, weil es zu gefährlich ist.",
                                     variable=radioValue2, value=4) 
        option4.pack()
        
        option5 = Radiobutton(window1,text="e) Die Feriengäste machen den Landwirten viel Arbeit.",
                                     variable=radioValue2, value=5) 
        option5.pack()
        
        # to measure time
        t_start5 = time.time()
        
        # destroy all options and pass time value
        next1_button['command'] = lambda: [press19(t_start5), option1.destroy(), 
                                           option2.destroy(), option3.destroy(), 
                                           option4.destroy(), option5.destroy()]
        
        next1_button.config(text="Eingabe bestätigen")    
        
        window1.title("Spiel1.3")
        
    def press18(t_start3):
        """
        Write solution and time in csv file.

        Input: t_start3 is the starting time
        """
        # to measure time
        t_end3 = time.time() - t_start3
        
        # get solution
        story_entry = radioValue1.get()   
        
        # write into csv file
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end3])

        # to measure time
        t_start4 = time.time()
        
        game1_label.config(text="Weiter zu Spiel 1.3.")
        
        next1_button.config(text="Bestätigen.")



        next1_button['command'] = lambda: press2(t_start4)
        
    def press1(t_start2):
        """
        Displays task and options.

        Input: t_start2 is the starting time
        """
        game1_label.config(text='Ein kinderfreundliches Rathaus\n \n \
        Seit einiger Zeit gibt es in Lippstadt in Nordrhein-Westfalen einen besonderen Telefondienst:\n \
        den heißen Draht für Kinder! Wenn zum Beispiel Autos zu schnell fahren, eine Ampel auf dem Schulweg\n \
        fehlt oder auf dem Spielplatz etwas nicht in Ordnung ist, dann können sich die Kinder direkt im Rathaus beschweren.\n \
        Lippstadt ist die erste Stadt in Deutschland, die einen solchen Telefondienst für Kinder eingerichtet hat.\n \
        Sie können an jedem Werktag zwischen 7 und 17 Uhr im Rathaus anrufen und alles vorbringen, was sie freut oder ärgert,\n \
        was ihnen Spaß oder Kummer macht. Alle Hinweise und Vorschläge der kleinen Bürger werden ernst genommen.\n \
        Wenn ein Kind die Nummer 400 wählt, dann meldet sich eine freundliche Stimme. “Hier ist das Kindertelefon“,\n \
        sagt Frau Cordes. Was die Kinder bedrückt und wie Frau Cordes versucht, ihnen zu helfen,zeigen einige Beispiele:\n \
        “Guten Tag, hier ist Birgit“, sagt die kleine Anruferin aufgeregt. “Ich bin eben in eine Glasscherbe getreten!“\n \
        Birgit erzählt, daß auf dem Spielplatz bei der Nicolai-Kirche die Scherben einer zerbrochenen Flasche liegen.\n \
        Frau Cordes verspricht Birgit, daß sie Hilfe schickt und daß diese Gefahr so schnell wie möglich beseitigt wird.\n \
        Zehn Minuten danach klagt ein Junge, daß er auf seinem Schulweg seit Wochen Angst hat, über die Hauptstraße zu gehen.\n \
        Die Autos fahren dort sehr schnell, und es gibt keine Ampel und kein Warnschild. Dagegen muß unbedingt etwas geschehen.\n \
        Dreißig Minuten später meldet sich noch ein Kind mit einem Verkehrsproblem. Die kleine Kristina\n \
        schlägt vor, zwei Kinder mitten auf die enge Straße vor ihrem Kindergarten zu malen.\n \
        Die Autofahrer wissen dann, daß kleine Kinder in der Nähe sind. Unter Umständen fahren sie dann in Zukunft vorsichtiger.\n \
        Kein Kind ruft vergebens an. Frau Cordes notiert sich alles, bedankt sich bei den Kindern\n \
        für die Anregungen und Informationen und verspricht Hilfe. Sie wird die Vorschläge an die\n \
        zuständigen Stellen weitergeben. Dann versuchen zum Beispiel die Verkehrsexperten, die\n \
        Hauptstraße für Kinder sicherer zu machen. Dabei werden sie auch über den Vorschlag nachdenken, Kinder auf die Straße zu malen.\n \
        Frau Cordes kümmert sich um jeden Vorschlag, jede Beschwerde und jeden Wunsch. Sie hilft auch\n \
        einem Mädchen, das eine Brieffreundin in England sucht. Sie macht aber keine falschen Versprechungen, wenn sie nicht helfen kann.\n \
        Die Idee, im Rathaus ein Telefon ausschließlich für Kinder einzurichten, hatte als erster der\n \
        Bürgermeister der Stadt. Auch die übrigen Kommunalpolitiker Lippstadts sind davon überzeugt,\n \
        daß man schon früh lernen soll, seine Rechte wahrzunehmen, und sie vermuten, dass das Kindertelefon\n \
        dazu eine gute Möglichkeit bietet. Seit es dieses Telefon gibt, haben bereits viele Kinder angerufen.\n \
        Die meisten waren zwischen sieben und elf Jahre alt.\n \
        Für das Kindertelefon in Lippstadt interessieren sich inzwischen auch andere Stadtverwaltungen.\n \
        Viele haben sich deshalb bereits erkundigt, welche Erfahrungen in Lippstadt gemacht wurden.\n \n \
        Welche ist die einzige wahre Aussage? Klicke die richtige Aussage an und bestätige.\n')
        
        # different solution options
        option1 = Radiobutton(window1,text="a) Es ist nicht gefährlich, die Hauptstraße zu überqueren, weil es dort eine Ampel gibt.",
                                     variable=radioValue1, value=1) 
        option1.pack()
 
        option2 = Radiobutton(window1,text="b) Die Kinder beklagen sich im Rathaus, wenn sie Probleme mit den Eltern haben.",
                                     variable=radioValue1, value=2) 
        option2.pack()
        
        option3 = Radiobutton(window1,text="c) Frau Cordes informiert den Bürgermeister nach Beschwerden der Kinder.",
                                     variable=radioValue1, value=3) 
        option3.pack()
        
        option4 = Radiobutton(window1,text="d) Kinder können jeden Tag von 8-17 Uhr Frau Cordes erreichen.",
                                     variable=radioValue1, value=4) 
        option4.pack()
        
        option5 = Radiobutton(window1,text="e) Der Bürgermeister schlug das Kindertelefon in Lippstadt vor.",
                                     variable=radioValue1, value=5) 
        option5.pack()
        
        # to measure time
        t_start3 = time.time()
        
        # destroy all options and pass time value
        next1_button['command'] = lambda: [press18(t_start3), option1.destroy(), 
                                           option2.destroy(), option3.destroy(), 
                                           option4.destroy(), option5.destroy()]
        
        window1.title("Spiel1.2")
        
    def press17(t_start1):
        """
        Write solution and time in csv file.

        Input: t_start1 is the starting time
        """
        # to measure time
        t_end3 = time.time() - t_start1
        
        # get solution
        story_entry = radioValue.get() 
        
        # write into csv file
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end3])

        # to measure time
        t_start2 = time.time()

        game1_label.config(text="Weiter zu Spiel 1.2.")
 
        next1_button.config(text="Bestätigen")
        


        next1_button['command'] = lambda: press1(t_start2)
        
    def press(t_start):
        """
        Displays task and options.

        Input: t_start is the starting time
        """
        # to measure time
        t_end1 = time.time() - t_start
        
        # get name
        story_entry = inputbox.get() 
              
        # write into csv file 
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end1])
            
        game1_label.config(text="Harald ist Hausmann\n \n \
        Wenn morgens der Wecker klingelt, steht Harald Müller als erster auf und macht das Frühstück.\n \
        Dann weckt er seine Frau und die beiden Kinder. Er ist Hausmann - und das schon seit sechs Jahren.\n \
        Damals, nach der Geburt des ersten Kindes, war für das Ehepaar nur eines klar. Einer von beiden\n \
        musste seinen Beruf aufgeben, um das Kind und den Haushalt zu versorgen.\n \
        Die Großeltern hätten zwar gern geholfen, aber sie wohnten zu weit entfernt.\n \
        Harald wurde als technischer Zeichner nicht besonders gut bezahlt. Seine Frau Christine verdiente\n \
        ein bisschen mehr. Sie war Krankenschwester und liebte ihren Beruf. Im Krankenhaus hatte man ihr\n \
        die Verantwortung für eine große Station übertragen. Deswegen fragte sie ihren Mann, ob er nicht\n \
        das Kind und den Haushalt versorgen wolle. Das Gespräch zwischen den beiden Eheleuten war sehr\n \
        ernst und dauerte lange. Aber zuletzt waren sie sich einig.\n \
        So also kam Harald zu seiner neuen Arbeit. Das bedeutete für ihn eine große Umstellung.\n \
        Er stammte aus einem Elternhaus, in dem die Rollen klar verteilt waren. Kein Mensch wäre dort\n \
        auf die Idee gekommen, dem Jungen beizubringen, wie man kocht und näht oder gar wie man ein\n \
        Baby versorgt. In Abendkursen an der Volkshochschule lernte er nun, leckere Mahlzeiten zu bereiten,\n \
        Wäsche zu flicken und Knöpfe anzunähen, und Christine zeigte ihm, wie man einen Säugling badet und wickelt.\n \
        Bald begriff er, daß das Führen eines Haushalts mit zwei Kindern ein richtiger Beruf ist,\n \
        der viel Wissen, Anstrengung und Zeit erfordert.\n \
        Haralds Tag ist ausgefüllt. Heute morgen hat er die Wäsche geflickt und das Essen gekocht.\n \
        Heute nachmittag muss er dem Sohn bei einer Hausaufgabe helfen und mit der Tochter zum Arzt gehen.\n \
        Die Kleine hat Halsschmerzen. Sie hat sich beim Baden erkältet. Sicher wird sie ein Medikament\n \
        aus der Apotheke brauchen. Danach muss Harald noch einige Lebensmittel einkaufen. Das macht ihm\n \
        am meisten Spaß. Er vergleicht die Preise und lässt sich nicht alles 'andrehen'. Der Fleischer,\n \
        der ihn zuerst für einen Junggesellen hielt und deswegen glaubte, ihm die schlechtesten Stücke\n \
        teuer verkaufen zu können, wird dies jetzt nicht mehr versuchen. Auch die Hausfrauen aus der\n \
        Nachbarschaft haben Respekt vor ihm wie er vor ihnen. Nur einige Männer schauen noch auf ihn herab.\n \
        Für sie ist er auf der sozialen Leiter nicht auf-, sondern abgestiegen. Doch Harald interessiert\n \
        sich nicht für das, was diese Nachbarn sagen. Er ist stolz darauf, dass er von den Hausfrauen\n \
        als 'Kollege' akzeptiert wird, denn er weiß, was für eine hohe Leistung diese Frauen jeden Tag\n \
        erbringen müssen.\n \n Welche ist die einzige wahre Aussage? Klicke die richtige Aussage an und bestätige.\n")
       
        # different solution options
        option1 = Radiobutton(window1,text="a) Christine ist Arzthelferin.",
                                     variable=radioValue, value=1) 
        option1.pack()
        
        option2 = Radiobutton(window1,text="b) Harald hat von Christine gelernt, wie man Knöpfe annäht.",
                                     variable=radioValue, value=2) 
        option2.pack()
        
        option3 = Radiobutton(window1,text="c) Harald musste zum Arzt gehen, weil sich seine Tochter erkältet hat.",
                                     variable=radioValue, value=3) 
        option3.pack()
        
        option4 = Radiobutton(window1,text="d) Harald ist stolz, dass er seine Kinder gut erzogen hat.",
                                     variable=radioValue, value=4) 
        option4.pack()
        
        option5 = Radiobutton(window1,text="e) Das Kochen macht Harald am meisten Spaß.",
                                     variable=radioValue, value=5) 
        option5.pack()

        # to measure time
        t_start1 = time.time()
        
        next1_button.config(text="Eingabe bestätigen")

        # destroy all options and pass time value
        next1_button['command'] = lambda: [press17(t_start1), option1.destroy(),
                                           option2.destroy(), option3.destroy(), 
                                           option4.destroy(), option5.destroy()]
        
        

        window1.title("Spiel1.1")
        
    
    # to measure time
    t_start = time.time() 
    next1_button = Button(window1, text="Bestätige deinen Namen und beginne Spiel 1.1.", command=lambda: [press(t_start), 
                                                                                    inputbox.destroy()])
    
    

    game1_label.pack()
    inputbox.pack()
    next1_button.pack()

###################################################
################### SECOND GAME ###################
###################################################
    
def game2():
    """
    opens first game window.
    
    """
    window2 = Toplevel() 
    window2.title("Anleitung Spiel 2")
    inputbox2 = Entry(window2, bd=5, width=40)
    game2_label = Label(window2, text="Es erscheinen 10 Bilder. \n \
    Merke dir in 10 Sekunden so viele von den Bildern wie möglich. \n \
    Im Anschluss erscheinen 20 Bilder, wovon du möglichst vielen von den 10 voher gesehenen Bildern auswählen sollst. \n \
    Klicke auf die richtigen Bilder und bestätige die Antwort mit dem Button. \n \
    Bewertet wird die Lösung und die benötigte Zeit.")
 

    
    # Solution of participant of each task of game 2
    window2.geometry('1400x1000')
    CheckbuttonValue1 = IntVar(window2)
    CheckbuttonValue2 = IntVar(window2)
    CheckbuttonValue3 = IntVar(window2)
    CheckbuttonValue4 = IntVar(window2)
    CheckbuttonValue5 = IntVar(window2)
    CheckbuttonValue6 = IntVar(window2)
    CheckbuttonValue7 = IntVar(window2)
    CheckbuttonValue8 = IntVar(window2)
    CheckbuttonValue9 = IntVar(window2)
    CheckbuttonValue10 = IntVar(window2)
    CheckbuttonValue11 = IntVar(window2)
    CheckbuttonValue12 = IntVar(window2)
    CheckbuttonValue13 = IntVar(window2)
    CheckbuttonValue14 = IntVar(window2)
    CheckbuttonValue15 = IntVar(window2)
    CheckbuttonValue16 = IntVar(window2)
    CheckbuttonValue17 = IntVar(window2)
    CheckbuttonValue18 = IntVar(window2)
    CheckbuttonValue19 = IntVar(window2)
    CheckbuttonValue20 = IntVar(window2)
    
    CheckbuttonValue21 = IntVar(window2)
    CheckbuttonValue22 = IntVar(window2)
    CheckbuttonValue23 = IntVar(window2)
    CheckbuttonValue24 = IntVar(window2)
    CheckbuttonValue25 = IntVar(window2)
    CheckbuttonValue26 = IntVar(window2)
    CheckbuttonValue27 = IntVar(window2)
    CheckbuttonValue28 = IntVar(window2)
    CheckbuttonValue29 = IntVar(window2)
    CheckbuttonValue30 = IntVar(window2)
    CheckbuttonValue31 = IntVar(window2)
    CheckbuttonValue32 = IntVar(window2)
    CheckbuttonValue33 = IntVar(window2)
    CheckbuttonValue34 = IntVar(window2)
    CheckbuttonValue35 = IntVar(window2)
    CheckbuttonValue36 = IntVar(window2)
    CheckbuttonValue37 = IntVar(window2)
    CheckbuttonValue38 = IntVar(window2)
    CheckbuttonValue39 = IntVar(window2)
    CheckbuttonValue40 = IntVar(window2)
    
    CheckbuttonValue41 = IntVar(window2)
    CheckbuttonValue42 = IntVar(window2)
    CheckbuttonValue43 = IntVar(window2)
    CheckbuttonValue44 = IntVar(window2)
    CheckbuttonValue45 = IntVar(window2)
    CheckbuttonValue46 = IntVar(window2)
    CheckbuttonValue47 = IntVar(window2)
    CheckbuttonValue48 = IntVar(window2)
    CheckbuttonValue49 = IntVar(window2)
    CheckbuttonValue50 = IntVar(window2)
    CheckbuttonValue51 = IntVar(window2)
    CheckbuttonValue52 = IntVar(window2)
    CheckbuttonValue53 = IntVar(window2)
    CheckbuttonValue54 = IntVar(window2)
    CheckbuttonValue55 = IntVar(window2)
    CheckbuttonValue56 = IntVar(window2)
    CheckbuttonValue57 = IntVar(window2)
    CheckbuttonValue58 = IntVar(window2)
    CheckbuttonValue59 = IntVar(window2)
    CheckbuttonValue60 = IntVar(window2)
    
    CheckbuttonValue61 = IntVar(window2)
    CheckbuttonValue62 = IntVar(window2)
    CheckbuttonValue63 = IntVar(window2)
    CheckbuttonValue64 = IntVar(window2)
    CheckbuttonValue65 = IntVar(window2)
    CheckbuttonValue66 = IntVar(window2)
    CheckbuttonValue67 = IntVar(window2)
    CheckbuttonValue68 = IntVar(window2)
    CheckbuttonValue69 = IntVar(window2)
    CheckbuttonValue70 = IntVar(window2)
    CheckbuttonValue71 = IntVar(window2)
    CheckbuttonValue72 = IntVar(window2)
    CheckbuttonValue73 = IntVar(window2)
    CheckbuttonValue74 = IntVar(window2)
    CheckbuttonValue75 = IntVar(window2)
    CheckbuttonValue76 = IntVar(window2)
    CheckbuttonValue77 = IntVar(window2)
    CheckbuttonValue78 = IntVar(window2)
    CheckbuttonValue79 = IntVar(window2)
    CheckbuttonValue80 = IntVar(window2)
    

    def press16(t_start16):
        """
        Write solution and time in csv file. End game 2.

        Input: t_start16 is the starting time
        """
        # to measure time
        t_end17 = time.time() - t_start16
       
        # get solution
        story_entry = [CheckbuttonValue61.get(), CheckbuttonValue62.get(), CheckbuttonValue63.get(), 
                       CheckbuttonValue64.get(), CheckbuttonValue65.get(), CheckbuttonValue66.get(), 
                       CheckbuttonValue67.get(), CheckbuttonValue68.get(), CheckbuttonValue69.get(), 
                       CheckbuttonValue70.get(), CheckbuttonValue71.get(), CheckbuttonValue72.get(), 
                       CheckbuttonValue73.get(), CheckbuttonValue74.get(), CheckbuttonValue75.get(), 
                       CheckbuttonValue76.get(), CheckbuttonValue77.get(), CheckbuttonValue78.get(), 
                       CheckbuttonValue79.get(), CheckbuttonValue80.get()]

        # write into csv file 
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end17])
            
  
      
        window16 = Tk()
        window16.title("EndeSpiel2")
        window16.geometry('600x200')
        # letztes window

    def press15(t_start15):
        """
        Displays 20 pictures to select the right solution.

        Input: t_start15 is the starting time
        """
        # to measure time
        t_end16 = time.time() - t_start15
        
        game2_label.config(text="Wähle so schnell wie möglich die 10 richtigen Bilder aus.")
      
        next2_button.config(text="Auswahl bestätigen.")
        
        # to measure time                    
        t_start16 = time.time()

        # to frame pictures
        border3 = Frame(window2)
        border3.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load = Image.open("images/test5.png") 
        resize_image = load.resize((190, 190))
        render = ImageTk.PhotoImage(resize_image)
        img = Checkbutton(border3, image=render,
                                     variable=CheckbuttonValue61, onvalue=1, offvalue=0) 
        img.pack(padx=30, pady=5, side=LEFT)
        
        load1 = Image.open("images/test31.png") 
        resize_image1 = load1.resize((190, 190))
        render1 = ImageTk.PhotoImage(resize_image1)
        img1 = Checkbutton(border3, image=render1,
                                     variable=CheckbuttonValue62, onvalue=2, offvalue=0) 
        img1.pack(padx=30, pady=5, side=LEFT)
        
        load2 = Image.open("images/test2.png") 
        resize_image2 = load2.resize((190, 190))
        render2 = ImageTk.PhotoImage(resize_image2)
        img2 = Checkbutton(border3, image=render2,
                                     variable=CheckbuttonValue63, onvalue=3, offvalue=0) 
        img2.pack(padx=30, pady=5, side=LEFT)
        
        load3 = Image.open("images/test49.png") 
        resize_image3 = load3.resize((190, 190))
        render3 = ImageTk.PhotoImage(resize_image3)
        img3 = Checkbutton(border3, image=render3,
                                     variable=CheckbuttonValue64, onvalue=4, offvalue=0) 
        img3.pack(padx=30, pady=5, side=LEFT)
        
        load4 = Image.open("images/test48.png") 
        resize_image4 = load4.resize((190, 190))
        render4 = ImageTk.PhotoImage(resize_image4)
        img4 = Checkbutton(border3, image=render4,
                                     variable=CheckbuttonValue65, onvalue=5, offvalue=0) 
        img4.pack(padx=30, pady=5, side=LEFT)
        
        border4 = Frame(window2)
        border4.pack(side='top', padx='5', pady='1')
        
        load5 = Image.open("images/test47.png") 
        resize_image5 = load5.resize((190, 190))
        render5 = ImageTk.PhotoImage(resize_image5)
        img5 = Checkbutton(border4, image=render5,
                                     variable=CheckbuttonValue66, onvalue=6, offvalue=0) 
        img5.pack(padx=30, pady=5, side=LEFT)
        
        load6 = Image.open("images/test53.png") 
        resize_image6 = load6.resize((190, 190))
        render6 = ImageTk.PhotoImage(resize_image6)
        img6 = Checkbutton(border4, image=render6,
                                     variable=CheckbuttonValue67, onvalue=7, offvalue=0) 
        img6.pack(padx=30, pady=5, side=LEFT)
        
        load7 = Image.open("images/test55.png") 
        resize_image7 = load7.resize((190, 190))
        render7 = ImageTk.PhotoImage(resize_image7)
        img7 = Checkbutton(border4, image=render7,
                                     variable=CheckbuttonValue68, onvalue=8, offvalue=0) 
        img7.pack(padx=30, pady=5, side=LEFT)
        
        load8 = Image.open("images/test34.png") 
        resize_image8 = load8.resize((190, 190))
        render8 = ImageTk.PhotoImage(resize_image8)
        img8 = Checkbutton(border4, image=render8,
                                     variable=CheckbuttonValue69, onvalue=9, offvalue=0) 
        img8.pack(padx=30, pady=5, side=LEFT)
        
        load9 = Image.open("images/test44.png") 
        resize_image9 = load9.resize((190, 190))
        render9 = ImageTk.PhotoImage(resize_image9)
        img9 = Checkbutton(border4, image=render9,
                                     variable=CheckbuttonValue70, onvalue=10, offvalue=0) 
        img9.pack(padx=30, pady=5, side=LEFT)
        
        border5 = Frame(window2)
        border5.pack(side='top', padx='5', pady='1')
        
        load10 = Image.open("images/test10.png") 
        resize_image10 = load10.resize((190, 190))
        render10 = ImageTk.PhotoImage(resize_image10)
        img10 = Checkbutton(border5, image=render10,
                                     variable=CheckbuttonValue71, onvalue=11, offvalue=0) 
        img10.pack(padx=30, pady=5, side=LEFT)
        
        load11 = Image.open("images/test30.png") 
        resize_image11 = load11.resize((190, 190))
        render11 = ImageTk.PhotoImage(resize_image11)
        img11 = Checkbutton(border5, image=render11,
                                     variable=CheckbuttonValue72, onvalue=12, offvalue=0) 
        img11.pack(padx=30, pady=5, side=LEFT)
        
        load12 = Image.open("images/test46.png") 
        resize_image12 = load12.resize((190, 190))
        render12 = ImageTk.PhotoImage(resize_image12)
        img12 = Checkbutton(border5, image=render12,
                                     variable=CheckbuttonValue73, onvalue=13, offvalue=0) 
        img12.pack(padx=30, pady=5, side=LEFT)
        
        load13 = Image.open("images/test19.png") 
        resize_image13 = load13.resize((190, 190))
        render13 = ImageTk.PhotoImage(resize_image13)
        img13 = Checkbutton(border5, image=render13,
                                     variable=CheckbuttonValue74, onvalue=14, offvalue=0) 
        img13.pack(padx=30, pady=5, side=LEFT)
        
        load14 = Image.open("images/test45.png") 
        resize_image14 = load14.resize((190, 190))
        render14 = ImageTk.PhotoImage(resize_image14)
        img14 = Checkbutton(border5, image=render14,
                                     variable=CheckbuttonValue75, onvalue=15, offvalue=0) 
        img14.pack(padx=30, pady=5, side=LEFT)
        
        border6 = Frame(window2)
        border6.pack(side='top', padx='5', pady='1')
        
        load15 = Image.open("images/test33.png") 
        resize_image15 = load15.resize((190, 190))
        render15 = ImageTk.PhotoImage(resize_image15)
        img15 = Checkbutton(border6, image=render15,
                                     variable=CheckbuttonValue76, onvalue=16, offvalue=0) 
        img15.pack(padx=30, pady=5, side=LEFT)
        
        load16 = Image.open("images/test26.png") 
        resize_image16 = load16.resize((190, 190))
        render16 = ImageTk.PhotoImage(resize_image16)
        img16 = Checkbutton(border6, image=render16,
                                     variable=CheckbuttonValue77, onvalue=17, offvalue=0) 
        img16.pack(padx=30, pady=5, side=LEFT)
        
        load17 = Image.open("images/test32.png") 
        resize_image17 = load17.resize((190, 190))
        render17 = ImageTk.PhotoImage(resize_image17)
        img17 = Checkbutton(border6, image=render17,
                                     variable=CheckbuttonValue78, onvalue=18, offvalue=0) 
        img17.pack(padx=30, pady=5, side=LEFT)
        
        load18 = Image.open("images/test12.png") 
        resize_image18 = load18.resize((190, 190))
        render18 = ImageTk.PhotoImage(resize_image18)
        img18 = Checkbutton(border6, image=render18,
                                     variable=CheckbuttonValue79, onvalue=19, offvalue=0) 
        img18.pack(padx=30, pady=5, side=LEFT)
        
        load19 = Image.open("images/test11.png") 
        resize_image19 = load19.resize((190, 190))
        render19 = ImageTk.PhotoImage(resize_image19)
        img19 = Checkbutton(border6, image=render19,
                                     variable=CheckbuttonValue80, onvalue=20, offvalue=0) 
        img19.pack(padx=30, pady=5, side=LEFT)
        
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img.destroy(), img1.destroy(), 
                                           img2.destroy(), img3.destroy(), 
                                           img4.destroy(), img5.destroy(), 
                                           img6.destroy(), img7.destroy(), 
                                           img8.destroy(), img9.destroy(), 
                                           img10.destroy(), img11.destroy(), 
                                           img12.destroy(), img13.destroy(), 
                                           img14.destroy(), img15.destroy(), 
                                           img16.destroy(), img17.destroy(), 
                                           img18.destroy(), img19.destroy(), 
                                           border3.destroy(), border4.destroy(), 
                                           border5.destroy(), border6.destroy(), 
                                           window2.destroy(), window.destroy(), 
                                           press16(t_start16)]
        
        window2.mainloop()

    def press14(t_start14):
        """
        Displays 10 pictures for 10 seconds.

        Input: t_start14 is the starting time
        """
        # to measure time
        t_end15 = time.time() - t_start14
       
        game2_label.config(text="Merke dir die Bilder. Zeit 10 Sekunden.")
        
        next2_button.config(text="Weiter zur Lösungsseite.")
        
        t_start15 = time.time()
        
        # to frame pictures
        border5 = Frame(window2)
        border5.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load20 = Image.open("images/test31.png") 
        resize_image20 = load20.resize((190, 190))
        render20 = ImageTk.PhotoImage(resize_image20)
        img20 = Label(border5, image=render20)
        img20.pack(padx=30, pady=5, side=LEFT)
        
        load21 = Image.open("images/test34.png") 
        resize_image21 = load21.resize((190, 190))
        render21 = ImageTk.PhotoImage(resize_image21)
        img21 = Label(border5, image=render21)
        img21.pack(padx=30, pady=5, side=LEFT)
        
        load22 = Image.open("images/test48.png") 
        resize_image22 = load22.resize((190, 190))
        render22 = ImageTk.PhotoImage(resize_image22)
        img22 = Label(border5, image=render22)
        img22.pack(padx=30, pady=5, side=LEFT)
        
        load23 = Image.open("images/test46.png") 
        resize_image23 = load23.resize((190, 190))
        render23 = ImageTk.PhotoImage(resize_image23)
        img23 = Label(border5, image=render23)
        img23.pack(padx=30, pady=5, side=LEFT)
        
        load24 = Image.open("images/test49.png") 
        resize_image24 = load24.resize((190, 190))
        render24 = ImageTk.PhotoImage(resize_image24)
        img24 = Label(border5, image=render24)
        img24.pack(padx=30, pady=5, side=LEFT)
        
        border6 = Frame(window2)
        border6.pack(side='top', padx='5', pady='1')
        
        load25 = Image.open("images/test47.png") 
        resize_image25 = load25.resize((190, 190))
        render25 = ImageTk.PhotoImage(resize_image25)
        img25 = Label(border6, image=render25)
        img25.pack(padx=30, pady=5, side=LEFT)
        
        load26 = Image.open("images/test33.png") 
        resize_image26 = load26.resize((190, 190))
        render26 = ImageTk.PhotoImage(resize_image26)
        img26 = Label(border6, image=render26)
        img26.pack(padx=30, pady=5, side=LEFT)
        
        load27 = Image.open("images/test45.png") 
        resize_image27 = load27.resize((190, 190))
        render27 = ImageTk.PhotoImage(resize_image27)
        img27 = Label(border6, image=render27)
        img27.pack(padx=30, pady=5, side=LEFT)
        
        load28 = Image.open("images/test32.png") 
        resize_image28 = load28.resize((190, 190))
        render28 = ImageTk.PhotoImage(resize_image28)
        img28 = Label(border6, image=render28)
        img28.pack(padx=30, pady=5, side=LEFT)
        
        load29 = Image.open("images/test30.png") 
        resize_image29 = load29.resize((190, 190))
        render29 = ImageTk.PhotoImage(resize_image29)
        img29 = Label(border6, image=render29)
        img29.pack(padx=30, pady=5, side=LEFT)
        
        # destroy all picutres after 10 seconds
        img20.after(10000, img20.destroy)
        img21.after(10000, img21.destroy)
        img22.after(10000, img22.destroy)
        img23.after(10000, img23.destroy)
        img24.after(10000, img24.destroy)
        img25.after(10000, img25.destroy)
        img26.after(10000, img26.destroy)
        img27.after(10000, img27.destroy)
        img28.after(10000, img28.destroy)
        img29.after(10000, img29.destroy)
        border5.after(10000, border5.destroy)
        border6.after(10000, border6.destroy)
        
        window2.title("Spiel2.4")     
        
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img20.destroy(), img21.destroy(), 
                                           img22.destroy(), img23.destroy(), 
                                           img24.destroy(), img25.destroy(), 
                                           img26.destroy(), img27.destroy(), 
                                           img28.destroy(), img29.destroy(), 
                                           border5.destroy(), border6.destroy(), 
                                           press15(t_start15)]
        window2.mainloop()
        
    def press13(t_start13):
        """
        Write solution and time in csv file.

        Input: t_start13 is the starting time
        """
        # to measure time
        t_end14 = time.time() - t_start13
        
        # get solution
        story_entry = [CheckbuttonValue41.get(), CheckbuttonValue42.get(), CheckbuttonValue43.get(), 
                       CheckbuttonValue44.get(), CheckbuttonValue45.get(), CheckbuttonValue46.get(), 
                       CheckbuttonValue47.get(), CheckbuttonValue48.get(), CheckbuttonValue49.get(), 
                       CheckbuttonValue50.get(), CheckbuttonValue51.get(), CheckbuttonValue52.get(), 
                       CheckbuttonValue53.get(), CheckbuttonValue54.get(), CheckbuttonValue55.get(), 
                       CheckbuttonValue56.get(), CheckbuttonValue57.get(), CheckbuttonValue58.get(), 
                       CheckbuttonValue59.get(), CheckbuttonValue60.get()]

        # write into csv file 
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end14])

        game2_label.config(text='Weiter zu Spiel 2.4.')
        
        # to measure time
        t_start14 = time.time()
        
   
        
        next2_button.config(text="Bestätigen.")

        next2_button['command'] = lambda: press14(t_start14)

    def press12(t_start12):
        """
        Displays 20 pictures to select the right solution.

        Input: t_start12 is the starting time
        """
        # to measure time
        t_end13 = time.time() - t_start12
       
        game2_label.config(text="Wähle so schnell wie möglich die 10 richtigen Bilder aus.")
        
        next2_button.config(text="Auswahl bestätigen.")
             
        # to measure time               
        t_start13 = time.time()
        
        # to frame pictures
        border3 = Frame(window2)
        border3.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load = Image.open("images/test21.png") 
        resize_image = load.resize((190, 190))
        render = ImageTk.PhotoImage(resize_image)
        img = Checkbutton(border3, image=render,
                                     variable=CheckbuttonValue41, onvalue=1, offvalue=0) 
        img.pack(padx=30, pady=5, side=LEFT)
        
        load1 = Image.open("images/test23.png") 
        resize_image1 = load1.resize((190, 190))
        render1 = ImageTk.PhotoImage(resize_image1)
        img1 = Checkbutton(border3, image=render1,
                                     variable=CheckbuttonValue42, onvalue=2, offvalue=0) 
        img1.pack(padx=30, pady=5, side=LEFT)
        
        load2 = Image.open("images/test30.png") 
        resize_image2 = load2.resize((190, 190))
        render2 = ImageTk.PhotoImage(resize_image2)
        img2 = Checkbutton(border3, image=render2,
                                     variable=CheckbuttonValue43, onvalue=3, offvalue=0) 
        img2.pack(padx=30, pady=5, side=LEFT)
        
        load3 = Image.open("images/test39.png") 
        resize_image3 = load3.resize((190, 190))
        render3 = ImageTk.PhotoImage(resize_image3)
        img3 = Checkbutton(border3, image=render3,
                                     variable=CheckbuttonValue44, onvalue=4, offvalue=0) 
        img3.pack(padx=30, pady=5, side=LEFT)
        
        load4 = Image.open("images/test36.png") 
        resize_image4 = load4.resize((190, 190))
        render4 = ImageTk.PhotoImage(resize_image4)
        img4 = Checkbutton(border3, image=render4,
                                     variable=CheckbuttonValue45, onvalue=5, offvalue=0) 
        img4.pack(padx=30, pady=5, side=LEFT)
        
        border4 = Frame(window2)
        border4.pack(side='top', padx='5', pady='1')
        
        load5 = Image.open("images/test24.png") 
        resize_image5 = load5.resize((190, 190))
        render5 = ImageTk.PhotoImage(resize_image5)
        img5 = Checkbutton(border4, image=render5,
                                     variable=CheckbuttonValue46, onvalue=6, offvalue=0) 
        img5.pack(padx=30, pady=5, side=LEFT)
        
        load6 = Image.open("images/test26.png") 
        resize_image6 = load6.resize((190, 190))
        render6 = ImageTk.PhotoImage(resize_image6)
        img6 = Checkbutton(border4, image=render6,
                                     variable=CheckbuttonValue47, onvalue=7, offvalue=0) 
        img6.pack(padx=30, pady=5, side=LEFT)
        
        load7 = Image.open("images/test62.png") 
        resize_image7 = load7.resize((190, 190))
        render7 = ImageTk.PhotoImage(resize_image7)
        img7 = Checkbutton(border4, image=render7,
                                     variable=CheckbuttonValue48, onvalue=8, offvalue=0) 
        img7.pack(padx=30, pady=5, side=LEFT)
        
        load8 = Image.open("images/test28.png") 
        resize_image8 = load8.resize((190, 190))
        render8 = ImageTk.PhotoImage(resize_image8)
        img8 = Checkbutton(border4, image=render8,
                                     variable=CheckbuttonValue49, onvalue=9, offvalue=0) 
        img8.pack(padx=30, pady=5, side=LEFT)
        
        load9 = Image.open("images/test22.png") 
        resize_image9 = load9.resize((190, 190))
        render9 = ImageTk.PhotoImage(resize_image9)
        img9 = Checkbutton(border4, image=render9,
                                     variable=CheckbuttonValue50, onvalue=10, offvalue=0) 
        img9.pack(padx=30, pady=5, side=LEFT)
        
        border5 = Frame(window2)
        border5.pack(side='top', padx='5', pady='1')
        
        load10 = Image.open("images/test20.png") 
        resize_image10 = load10.resize((190, 190))
        render10 = ImageTk.PhotoImage(resize_image10)
        img10 = Checkbutton(border5, image=render10,
                                     variable=CheckbuttonValue51, onvalue=11, offvalue=0) 
        img10.pack(padx=30, pady=5, side=LEFT)
        
        load11 = Image.open("images/test37.png") 
        resize_image11 = load11.resize((190, 190))
        render11 = ImageTk.PhotoImage(resize_image11)
        img11 = Checkbutton(border5, image=render11,
                                     variable=CheckbuttonValue52, onvalue=12, offvalue=0) 
        img11.pack(padx=30, pady=5, side=LEFT)
        
        load12 = Image.open("images/test44.png") 
        resize_image12 = load12.resize((190, 190))
        render12 = ImageTk.PhotoImage(resize_image12)
        img12 = Checkbutton(border5, image=render12,
                                     variable=CheckbuttonValue53, onvalue=13, offvalue=0) 
        img12.pack(padx=30, pady=5, side=LEFT)
        
        load13 = Image.open("images/test12.png")
        resize_image13 = load13.resize((190, 190))
        render13 = ImageTk.PhotoImage(resize_image13)
        img13 = Checkbutton(border5, image=render13,
                                     variable=CheckbuttonValue54, onvalue=14, offvalue=0) 
        img13.pack(padx=30, pady=5, side=LEFT)
        
        load14 = Image.open("images/test38.png") 
        resize_image14 = load14.resize((190, 190))
        render14 = ImageTk.PhotoImage(resize_image14)
        img14 = Checkbutton(border5, image=render14,
                                     variable=CheckbuttonValue55, onvalue=15, offvalue=0) 
        img14.pack(padx=30, pady=5, side=LEFT)
        
        border6 = Frame(window2)
        border6.pack(side='top', padx='5', pady='1')
        
        load15 = Image.open("images/test55.png") 
        resize_image15 = load15.resize((190, 190))
        render15 = ImageTk.PhotoImage(resize_image15)
        img15 = Checkbutton(border6, image=render15,
                                     variable=CheckbuttonValue56, onvalue=16, offvalue=0) 
        img15.pack(padx=30, pady=5, side=LEFT)
        
        load16 = Image.open("images/test35.png") 
        resize_image16 = load16.resize((190, 190))
        render16 = ImageTk.PhotoImage(resize_image16)
        img16 = Checkbutton(border6, image=render16,
                                     variable=CheckbuttonValue57, onvalue=17, offvalue=0) 
        img16.pack(padx=30, pady=5, side=LEFT)
        
        load17 = Image.open("images/test33.png") 
        resize_image17 = load17.resize((190, 190))
        render17 = ImageTk.PhotoImage(resize_image17)
        img17 = Checkbutton(border6, image=render17,
                                     variable=CheckbuttonValue58, onvalue=18, offvalue=0) 
        img17.pack(padx=30, pady=5, side=LEFT)
        
        load18 = Image.open("images/test17.png") 
        resize_image18 = load18.resize((190, 190))
        render18 = ImageTk.PhotoImage(resize_image18)
        img18 = Checkbutton(border6, image=render18,
                                     variable=CheckbuttonValue59, onvalue=19, offvalue=0) 
        img18.pack(padx=30, pady=5, side=LEFT)
        
        load19 = Image.open("images/test18.png")     
        resize_image19 = load19.resize((190, 190))
        render19 = ImageTk.PhotoImage(resize_image19)
        img19 = Checkbutton(border6, image=render19,
                                     variable=CheckbuttonValue60, onvalue=20, offvalue=0) 
        img19.pack(padx=30, pady=5, side=LEFT)
        
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img.destroy(), img1.destroy(), 
                                           img2.destroy(), img3.destroy(), 
                                           img4.destroy(), img5.destroy(), 
                                           img6.destroy(), img7.destroy(), 
                                           img8.destroy(), img9.destroy(), 
                                           img10.destroy(), img11.destroy(), 
                                           img12.destroy(), img13.destroy(), 
                                           img14.destroy(), img15.destroy(), 
                                           img16.destroy(), img17.destroy(), 
                                           img18.destroy(), img19.destroy(), 
                                           border3.destroy(), border4.destroy(), 
                                           border5.destroy(), border6.destroy(), 
                                           press13(t_start13)]
        
        window2.mainloop()

    def press11(t_start11):
        """
        Displays 10 pictures for 10 seconds.

        Input: t_start11 is the starting time
        """
        # to measure time
        t_end12 = time.time() - t_start11
  
        game2_label.config(text="Merke dir die Bilder. Zeit 10 Sekunden.")
        
        next2_button.config(text="Weiter zur Lösungsseite.")
        
        # to measure time
        t_start12 = time.time()
        
        # to frame pictures
        border5 = Frame(window2)
        border5.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load20 = Image.open("images/test39.png") 
        resize_image20 = load20.resize((190, 190))
        render20 = ImageTk.PhotoImage(resize_image20)
        img20 = Label(border5, image=render20)
        img20.pack(padx=30, pady=5, side=LEFT)
        
        load21 = Image.open("images/test36.png") 
        resize_image21 = load21.resize((190, 190))
        render21 = ImageTk.PhotoImage(resize_image21)
        img21 = Label(border5, image=render21)
        img21.pack(padx=30, pady=5, side=LEFT)
        
        load22 = Image.open("images/test21.png") 
        resize_image22 = load22.resize((190, 190))
        render22 = ImageTk.PhotoImage(resize_image22)
        img22 = Label(border5, image=render22)
        img22.pack(padx=30, pady=5, side=LEFT)
        
        load23 = Image.open("images/test37.png") 
        resize_image23 = load23.resize((190, 190))
        render23 = ImageTk.PhotoImage(resize_image23)
        img23 = Label(border5, image=render23)
        img23.pack(padx=30, pady=5, side=LEFT)
        
        load24 = Image.open("images/test23.png") 
        resize_image24 = load24.resize((190, 190))
        render24 = ImageTk.PhotoImage(resize_image24)
        img24 = Label(border5, image=render24)
        img24.pack(padx=30, pady=5, side=LEFT)
        
        border6 = Frame(window2)
        border6.pack(side='top', padx='5', pady='1')
        
        load25 = Image.open("images/test20.png") 
        resize_image25 = load25.resize((190, 190))
        render25 = ImageTk.PhotoImage(resize_image25)
        img25 = Label(border6, image=render25)
        img25.pack(padx=30, pady=5, side=LEFT)
        
        load26 = Image.open("images/test22.png") 
        resize_image26 = load26.resize((190, 190))
        render26 = ImageTk.PhotoImage(resize_image26)
        img26 = Label(border6, image=render26)
        img26.pack(padx=30, pady=5, side=LEFT)
        
        load27 = Image.open("images/test38.png") 
        resize_image27 = load27.resize((190, 190))
        render27 = ImageTk.PhotoImage(resize_image27)
        img27 = Label(border6, image=render27)
        img27.pack(padx=30, pady=5, side=LEFT)
        
        load28 = Image.open("images/test24.png") 
        resize_image28 = load28.resize((190, 190))
        render28 = ImageTk.PhotoImage(resize_image28)
        img28 = Label(border6, image=render28)
        img28.pack(padx=30, pady=5, side=LEFT)
        
        load29 = Image.open("images/test35.png") 
        resize_image29 = load29.resize((190, 190))
        render29 = ImageTk.PhotoImage(resize_image29)
        img29 = Label(border6, image=render29)
        img29.pack(padx=30, pady=5, side=LEFT)
        
        # destroy all picutres after 10 seconds
        img20.after(10000, img20.destroy)
        img21.after(10000, img21.destroy)
        img22.after(10000, img22.destroy)
        img23.after(10000, img23.destroy)
        img24.after(10000, img24.destroy)
        img25.after(10000, img25.destroy)
        img26.after(10000, img26.destroy)
        img27.after(10000, img27.destroy)
        img28.after(10000, img28.destroy)
        img29.after(10000, img29.destroy)
        border5.after(10000, border5.destroy)
        border6.after(10000, border6.destroy)
        
        window2.title("Spiel2.3")      
        
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img20.destroy(), img21.destroy(), 
                                           img22.destroy(), img23.destroy(), 
                                           img24.destroy(), img25.destroy(), 
                                           img26.destroy(), img27.destroy(), 
                                           img28.destroy(), img29.destroy(), 
                                           border5.destroy(), border6.destroy(), 
                                           press12(t_start12)]
        window2.mainloop()
        
    def press10(t_start10):
        """
        Write solution and time in csv file.

        Input: t_start10 is the starting time
        """
        # to measure time
        t_end11 = time.time() - t_start10
        
        # get solution
        story_entry = [CheckbuttonValue21.get(), CheckbuttonValue22.get(), CheckbuttonValue23.get(), 
                       CheckbuttonValue24.get(), CheckbuttonValue25.get(), CheckbuttonValue26.get(), 
                       CheckbuttonValue27.get(), CheckbuttonValue28.get(), CheckbuttonValue29.get(), 
                       CheckbuttonValue30.get(), CheckbuttonValue31.get(), CheckbuttonValue32.get(), 
                       CheckbuttonValue33.get(), CheckbuttonValue34.get(), CheckbuttonValue35.get(), 
                       CheckbuttonValue36.get(), CheckbuttonValue37.get(), CheckbuttonValue38.get(), 
                       CheckbuttonValue39.get(), CheckbuttonValue40.get()]

        # write into csv file 
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end11])

  
        game2_label.config(text='Weiter zu Spiel 2.3.')
        t_start11 = time.time()
        
   
        
        next2_button.config(text="Bestätigen.")

        next2_button['command'] = lambda: press11(t_start11)
        
    def press9(t_start9):
        """
        Displays 20 pictures to select the right solution.

        Input: t_start9 is the starting time
        """
        # to measure time
        t_end10 = time.time() - t_start9
 
        game2_label.config(text="Wähle so schnell wie möglich die 10 richtigen Bilder aus.")
        
        next2_button.config(text="Auswahl bestätigen.")
           
        # to measure time                 
        t_start10 = time.time()
        
        # to frame pictures
        border7 = Frame(window2)
        border7.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load30 = Image.open("images/test5.png")
        resize_image30 = load30.resize((190, 190))
        render30 = ImageTk.PhotoImage(resize_image30)
        img30 = Checkbutton(border7, image=render30,
                                     variable=CheckbuttonValue21, onvalue=1, offvalue=0) 
        img30.pack(padx=30, pady=5, side=LEFT)
        
        load31 = Image.open("images/test11.png") 
        resize_image31 = load31.resize((190, 190))
        render31 = ImageTk.PhotoImage(resize_image31)
        img31 = Checkbutton(border7, image=render31,
                                     variable=CheckbuttonValue22, onvalue=2, offvalue=0) 
        img31.pack(padx=30, pady=5, side=LEFT)
        
        load32 = Image.open("images/test4.png") 
        resize_image32 = load32.resize((190, 190))
        render32 = ImageTk.PhotoImage(resize_image32)
        img32 = Checkbutton(border7, image=render32,
                                     variable=CheckbuttonValue23, onvalue=3, offvalue=0) 
        img32.pack(padx=30, pady=5, side=LEFT)
        
        load33 = Image.open("images/test13.png") 
        resize_image33 = load33.resize((190, 190))
        render33 = ImageTk.PhotoImage(resize_image33)
        img33 = Checkbutton(border7, image=render33,
                                     variable=CheckbuttonValue24, onvalue=4, offvalue=0) 
        img33.pack(padx=30, pady=5, side=LEFT)
        
        load34 = Image.open("images/test15.png") 
        resize_image34 = load34.resize((190, 190))
        render34 = ImageTk.PhotoImage(resize_image34)
        img34 = Checkbutton(border7, image=render34,
                                     variable=CheckbuttonValue25, onvalue=5, offvalue=0) 
        img34.pack(padx=30, pady=5, side=LEFT)
        
        border8 = Frame(window2)
        border8.pack(side='top', padx='5', pady='1')
        
        load35 = Image.open("images/test51.png") 
        resize_image35 = load35.resize((190, 190))
        render35 = ImageTk.PhotoImage(resize_image35)
        img35 = Checkbutton(border8, image=render35,
                                     variable=CheckbuttonValue26, onvalue=6, offvalue=0) 
        img35.pack(padx=30, pady=5, side=LEFT)
        
        load36 = Image.open("images/test56.png") 
        resize_image36 = load36.resize((190, 190))
        render36 = ImageTk.PhotoImage(resize_image36)
        img36 = Checkbutton(border8, image=render36,
                                     variable=CheckbuttonValue27, onvalue=7, offvalue=0) 
        img36.pack(padx=30, pady=5, side=LEFT)
        
        load37 = Image.open("images/test46.png")
        resize_image37 = load37.resize((190, 190))
        render37 = ImageTk.PhotoImage(resize_image37)
        img37 = Checkbutton(border8, image=render37,
                                     variable=CheckbuttonValue28, onvalue=8, offvalue=0) 
        img37.pack(padx=30, pady=5, side=LEFT)
        
        load38 = Image.open("images/test55.png") 
        resize_image38 = load38.resize((190, 190))
        render38 = ImageTk.PhotoImage(resize_image38)
        img38 = Checkbutton(border8, image=render38,
                                     variable=CheckbuttonValue29, onvalue=9, offvalue=0) 
        img38.pack(padx=30, pady=5, side=LEFT)
        
        load39 = Image.open("images/test16.png")   
        resize_image39 = load39.resize((190, 190))
        render39 = ImageTk.PhotoImage(resize_image39)
        img39 = Checkbutton(border8, image=render39,
                                     variable=CheckbuttonValue30, onvalue=10, offvalue=0) 
        img39.pack(padx=30, pady=5, side=LEFT)
        
        border9 = Frame(window2)
        border9.pack(side='top', padx='5', pady='1')
        
        load40 = Image.open("images/test10.png") 
        resize_image40 = load40.resize((190, 190))
        render40 = ImageTk.PhotoImage(resize_image40)
        img40 = Checkbutton(border9, image=render40,
                                     variable=CheckbuttonValue31, onvalue=11, offvalue=0) 
        img40.pack(padx=30, pady=5, side=LEFT)
        
        load41 = Image.open("images/test18.png") 
        resize_image41 = load41.resize((190, 190))
        render41 = ImageTk.PhotoImage(resize_image41)
        img41 = Checkbutton(border9, image=render41,
                                     variable=CheckbuttonValue32, onvalue=12, offvalue=0) 
        img41.pack(padx=30, pady=5, side=LEFT)
        
        load42 = Image.open("images/test14.png") 
        resize_image42 = load42.resize((190, 190))
        render42 = ImageTk.PhotoImage(resize_image42)
        img42 = Checkbutton(border9, image=render42,
                                     variable=CheckbuttonValue33, onvalue=13, offvalue=0) 
        img42.pack(padx=30, pady=5, side=LEFT)
        
        load43 = Image.open("images/test19.png")
        resize_image43 = load43.resize((190, 190))
        render43 = ImageTk.PhotoImage(resize_image43)
        img43 = Checkbutton(border9, image=render43,
                                     variable=CheckbuttonValue34, onvalue=14, offvalue=0) 
        img43.pack(padx=30, pady=5, side=LEFT)
        
        load44 = Image.open("images/test44.png") 
        resize_image44 = load44.resize((190, 190))
        render44 = ImageTk.PhotoImage(resize_image44)
        img44 = Checkbutton(border9, image=render44,
                                     variable=CheckbuttonValue35, onvalue=15, offvalue=0) 
        img44.pack(padx=30, pady=5, side=LEFT)
        
        border10 = Frame(window2)
        border10.pack(side='top', padx='5', pady='1')
        
        load45 = Image.open("images/test28.png") 
        resize_image45 = load45.resize((190, 190))
        render45 = ImageTk.PhotoImage(resize_image45)
        img45 = Checkbutton(border10, image=render45,
                                     variable=CheckbuttonValue36, onvalue=16, offvalue=0) 
        img45.pack(padx=30, pady=5, side=LEFT)
        
        load46 = Image.open("images/test29.png") 
        resize_image46 = load46.resize((190, 190))
        render46 = ImageTk.PhotoImage(resize_image46)
        img46 = Checkbutton(border10, image=render46,
                                     variable=CheckbuttonValue37, onvalue=17, offvalue=0) 
        img46.pack(padx=30, pady=5, side=LEFT)
        
        load47 = Image.open("images/test12.png") 
        resize_image47 = load47.resize((190, 190))
        render47 = ImageTk.PhotoImage(resize_image47)
        img47 = Checkbutton(border10, image=render47,
                                     variable=CheckbuttonValue38, onvalue=18, offvalue=0) 
        img47.pack(padx=30, pady=5, side=LEFT)
        
        load48 = Image.open("images/test17.png") 
        resize_image48 = load48.resize((190, 190))
        render48 = ImageTk.PhotoImage(resize_image48)
        img48 = Checkbutton(border10, image=render48,
                                     variable=CheckbuttonValue39, onvalue=19, offvalue=0) 
        img48.pack(padx=30, pady=5, side=LEFT)
        
        load49 = Image.open("images/test33.png") 
        resize_image49 = load49.resize((190, 190))
        render49 = ImageTk.PhotoImage(resize_image49)
        img49 = Checkbutton(border10, image=render49,
                                     variable=CheckbuttonValue40, onvalue=20, offvalue=0) 
        img49.pack(padx=30, pady=5, side=LEFT)
       
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img30.destroy(), img31.destroy(), 
                                           img32.destroy(), img33.destroy(), 
                                           img34.destroy(), img35.destroy(), 
                                           img36.destroy(), img37.destroy(), 
                                           img38.destroy(), img39.destroy(), 
                                           img40.destroy(), img41.destroy(), 
                                           img42.destroy(), img43.destroy(), 
                                           img44.destroy(), img45.destroy(), 
                                           img46.destroy(), img47.destroy(), 
                                           img48.destroy(), img49.destroy(), 
                                           border7.destroy(), border8.destroy(), 
                                           border9.destroy(), border10.destroy(), 
                                           press10(t_start10)]
        
        window2.mainloop()

    def press8(t_start8):
        """
        Displays 10 pictures for 10 seconds.

        Input: t_start8 is the starting time
        """
        # to measure time
        t_end9 = time.time() - t_start8
 
        game2_label.config(text="Merke dir die Bilder. Zeit 10 Sekunden.")
        
        next2_button.config(text="Weiter zur Lösungsseite.")
        
        # to measure time
        t_start9 = time.time()
        
        # to frame pictures
        border5 = Frame(window2)
        border5.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load20 = Image.open("images/test11.png") 
        resize_image20 = load20.resize((190, 190))
        render20 = ImageTk.PhotoImage(resize_image20)
        img20 = Label(border5, image=render20)
        img20.pack(padx=30, pady=5, side=LEFT)

        load21 = Image.open("images/test13.png") 
        resize_image21 = load21.resize((190, 190))
        render21 = ImageTk.PhotoImage(resize_image21)
        img21 = Label(border5, image=render21)
        img21.pack(padx=30, pady=5, side=LEFT)

        load22 = Image.open("images/test15.png") 
        resize_image22 = load22.resize((190, 190))
        render22 = ImageTk.PhotoImage(resize_image22)
        img22 = Label(border5, image=render22)
        img22.pack(padx=30, pady=5, side=LEFT)
        
        load23 = Image.open("images/test14.png") 
        resize_image23 = load23.resize((190, 190))
        render23 = ImageTk.PhotoImage(resize_image23)
        img23 = Label(border5, image=render23)
        img23.pack(padx=30, pady=5, side=LEFT)
        
        load24 = Image.open("images/test17.png") 
        resize_image24 = load24.resize((190, 190))
        render24 = ImageTk.PhotoImage(resize_image24)
        img24 = Label(border5, image=render24)
        img24.pack(padx=30, pady=5, side=LEFT)
        
        border6 = Frame(window2)
        border6.pack(side='top', padx='5', pady='1')
        
        load25 = Image.open("images/test18.png") 
        resize_image25 = load25.resize((190, 190))
        render25 = ImageTk.PhotoImage(resize_image25)
        img25 = Label(border6, image=render25)
        img25.pack(padx=30, pady=5, side=LEFT)
        
        load26 = Image.open("images/test12.png") 
        resize_image26 = load26.resize((190, 190))
        render26 = ImageTk.PhotoImage(resize_image26)
        img26 = Label(border6, image=render26)
        img26.pack(padx=30, pady=5, side=LEFT)
        
        load27 = Image.open("images/test19.png") 
        resize_image27 = load27.resize((190, 190))
        render27 = ImageTk.PhotoImage(resize_image27)
        img27 = Label(border6, image=render27)
        img27.pack(padx=30, pady=5, side=LEFT)
        
        load28 = Image.open("images/test10.png") 
        resize_image28 = load28.resize((190, 190))
        render28 = ImageTk.PhotoImage(resize_image28)
        img28 = Label(border6, image=render28)
        img28.pack(padx=30, pady=5, side=LEFT)
        
        load29 = Image.open("images/test16.png") 
        resize_image29 = load29.resize((190, 190))
        render29 = ImageTk.PhotoImage(resize_image29)
        img29 = Label(border6, image=render29)
        img29.pack(padx=30, pady=5, side=LEFT)
        
        # destroy all picutres after 10 seconds
        img20.after(10000, img20.destroy)
        img21.after(10000, img21.destroy)
        img22.after(10000, img22.destroy)
        img23.after(10000, img23.destroy)
        img24.after(10000, img24.destroy)
        img25.after(10000, img25.destroy)
        img26.after(10000, img26.destroy)
        img27.after(10000, img27.destroy)
        img28.after(10000, img28.destroy)
        img29.after(10000, img29.destroy)
        border5.after(10000, border5.destroy)
        border6.after(10000, border6.destroy)
        
        window2.title("Spiel2.2")
        
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img20.destroy(), img21.destroy(), 
                                           img22.destroy(), img23.destroy(), 
                                           img24.destroy(), img25.destroy(), 
                                           img26.destroy(), img27.destroy(), 
                                           img28.destroy(), img29.destroy(), 
                                           border5.destroy(), border6.destroy(), 
                                           press9(t_start9)]
        window2.mainloop()
    
    def press7(t_start7):
        """
        Write solution and time in csv file.

        Input: t_start7 is the starting time
        """
        # to measure time
        t_end8 = time.time() - t_start7
        
        # get solution
        story_entry = [CheckbuttonValue1.get(), CheckbuttonValue2.get(), CheckbuttonValue3.get(), 
                       CheckbuttonValue4.get(), CheckbuttonValue5.get(), CheckbuttonValue6.get(), 
                       CheckbuttonValue7.get(), CheckbuttonValue8.get(), CheckbuttonValue9.get(), 
                       CheckbuttonValue10.get(), CheckbuttonValue11.get(), CheckbuttonValue12.get(), 
                       CheckbuttonValue13.get(), CheckbuttonValue14.get(), CheckbuttonValue15.get(), 
                       CheckbuttonValue16.get(), CheckbuttonValue17.get(), CheckbuttonValue18.get(), 
                       CheckbuttonValue19.get(), CheckbuttonValue20.get()]

        # write into csv file 
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([story_entry,t_end8])

        game2_label.config(text='Weiter zu Spiel 2.2.')
        
        # to measure time
        t_start8 = time.time()
        
      
        next2_button.config(text="Bestätigen.")


        next2_button['command'] = lambda: press8(t_start8)

    def press6(t_start6):
        """
        Displays 20 pictures to select the right solution.

        Input: t_start6 is the starting time
        """
        # to measure time
        t_end7 = time.time() - t_start6
        
        game2_label.config(text="Wähle so schnell wie möglich die 10 richtigen Bilder aus.")

        next2_button.config(text="Auswahl bestätigen.")
        
        # to measure time
        t_start7 = time.time()

        # to frame pictures
        border3 = Frame(window2)
        border3.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load = Image.open("images/test20.png") 
        resize_image = load.resize((190, 190))
        render = ImageTk.PhotoImage(resize_image)
        img = Checkbutton(border3, image=render,
                                     variable=CheckbuttonValue1, onvalue=1, offvalue=0) 
        img.pack(padx=30, pady=5, side=LEFT)
        
        load1 = Image.open("images/test3.png") 
        resize_image1 = load1.resize((190, 190))
        render1 = ImageTk.PhotoImage(resize_image1)
        img1 = Checkbutton(border3, image=render1,
                                     variable=CheckbuttonValue2, onvalue=2, offvalue=0) 
        img1.pack(padx=30, pady=5, side=LEFT)
        
        load2 = Image.open("images/test9.png") 
        resize_image2 = load2.resize((190, 190))
        render2 = ImageTk.PhotoImage(resize_image2)
        img2 = Checkbutton(border3, image=render2,
                                     variable=CheckbuttonValue3, onvalue=3, offvalue=0) 
        img2.pack(padx=30, pady=5, side=LEFT)
        
        load3 = Image.open("images/test6.png") 
        resize_image3 = load3.resize((190, 190))
        render3 = ImageTk.PhotoImage(resize_image3)
        img3 = Checkbutton(border3, image=render3,
                                     variable=CheckbuttonValue4, onvalue=4, offvalue=0) 
        img3.pack(padx=30, pady=5, side=LEFT)
        
        load4 = Image.open("images/test45.png") 
        resize_image4 = load4.resize((190, 190))
        render4 = ImageTk.PhotoImage(resize_image4)
        img4 = Checkbutton(border3, image=render4,
                                     variable=CheckbuttonValue5, onvalue=5, offvalue=0) 
        img4.pack(padx=30, pady=5, side=LEFT)
        
        border4 = Frame(window2)
        border4.pack(side='top', padx='5', pady='1')
        
        load5 = Image.open("images/test29.png") 
        resize_image5 = load5.resize((190, 190))
        render5 = ImageTk.PhotoImage(resize_image5)
        img5 = Checkbutton(border4, image=render5,
                                     variable=CheckbuttonValue6, onvalue=6, offvalue=0) 
        img5.pack(padx=30, pady=5, side=LEFT)
        
        load6 = Image.open("images/test25.png") 
        resize_image6 = load6.resize((190, 190))
        render6 = ImageTk.PhotoImage(resize_image6)
        img6 = Checkbutton(border4, image=render6,
                                     variable=CheckbuttonValue7, onvalue=7, offvalue=0) 
        img6.pack(padx=30, pady=5, side=LEFT)
        
        load7 = Image.open("images/test15.png") 
        resize_image7 = load7.resize((190, 190))
        render7 = ImageTk.PhotoImage(resize_image7)
        img7 = Checkbutton(border4, image=render7,
                                     variable=CheckbuttonValue8, onvalue=8, offvalue=0) 
        img7.pack(padx=30, pady=5, side=LEFT)
        
        load8 = Image.open("images/test1.png") 
        resize_image8 = load8.resize((190, 190))
        render8 = ImageTk.PhotoImage(resize_image8)
        img8 = Checkbutton(border4, image=render8,
                                     variable=CheckbuttonValue9, onvalue=9, offvalue=0) 
        img8.pack(padx=30, pady=5, side=LEFT)
        
        load9 = Image.open("images/test4.png") 
        resize_image9 = load9.resize((190, 190))
        render9 = ImageTk.PhotoImage(resize_image9)
        img9 = Checkbutton(border4, image=render9,
                                     variable=CheckbuttonValue10, onvalue=10, offvalue=0) 
        img9.pack(padx=30, pady=5, side=LEFT)
        
        border5 = Frame(window2)
        border5.pack(side='top', padx='5', pady='1')
        
        load10 = Image.open("images/test16.png") 
        resize_image10 = load10.resize((190, 190))
        render10 = ImageTk.PhotoImage(resize_image10)
        img10 = Checkbutton(border5, image=render10,
                                     variable=CheckbuttonValue11, onvalue=11, offvalue=0) 
        img10.pack(padx=30, pady=5, side=LEFT)
        
        load11 = Image.open("images/test22.png") 
        resize_image11 = load11.resize((190, 190))
        render11 = ImageTk.PhotoImage(resize_image11)
        img11 = Checkbutton(border5, image=render11,
                                     variable=CheckbuttonValue12, onvalue=12, offvalue=0) 
        img11.pack(padx=30, pady=5, side=LEFT)
        
        load12 = Image.open("images/test5.png") 
        resize_image12 = load12.resize((190, 190))
        render12 = ImageTk.PhotoImage(resize_image12)
        img12 = Checkbutton(border5, image=render12,
                                     variable=CheckbuttonValue13, onvalue=13, offvalue=0) 
        img12.pack(padx=30, pady=5, side=LEFT)
        
        load13 = Image.open("images/test8.png") 
        resize_image13 = load13.resize((190, 190))
        render13 = ImageTk.PhotoImage(resize_image13)
        img13 = Checkbutton(border5, image=render13,
                                     variable=CheckbuttonValue14, onvalue=14, offvalue=0) 
        img13.pack(padx=30, pady=5, side=LEFT)
        
        load14 = Image.open("images/test50.png") 
        resize_image14 = load14.resize((190, 190))
        render14 = ImageTk.PhotoImage(resize_image14)
        img14 = Checkbutton(border5, image=render14,
                                     variable=CheckbuttonValue15, onvalue=15, offvalue=0) 
        img14.pack(padx=30, pady=5, side=LEFT)
        
        border6 = Frame(window2)
        border6.pack(side='top', padx='5', pady='1')
        
        load15 = Image.open("images/test23.png") 
        resize_image15 = load15.resize((190, 190))
        render15 = ImageTk.PhotoImage(resize_image15)
        img15 = Checkbutton(border6, image=render15,
                                     variable=CheckbuttonValue16, onvalue=16, offvalue=0) 
        img15.pack(padx=30, pady=5, side=LEFT)
        
        load16 = Image.open("images/test2.png") 
        resize_image16 = load16.resize((190, 190))
        render16 = ImageTk.PhotoImage(resize_image16)
        img16 = Checkbutton(border6, image=render16,
                                     variable=CheckbuttonValue17, onvalue=17, offvalue=0) 
        img16.pack(padx=30, pady=5, side=LEFT)
        
        load17 = Image.open("images/test.png") 
        resize_image17 = load17.resize((190, 190))
        render17 = ImageTk.PhotoImage(resize_image17)
        img17 = Checkbutton(border6, image=render17,
                                     variable=CheckbuttonValue18, onvalue=18, offvalue=0) 
        img17.pack(padx=30, pady=5, side=LEFT)
        
        load18 = Image.open("images/test11.png") 
        resize_image18 = load18.resize((190, 190))
        render18 = ImageTk.PhotoImage(resize_image18)
        img18 = Checkbutton(border6, image=render18,
                                     variable=CheckbuttonValue19, onvalue=19, offvalue=0) 
        img18.pack(padx=30, pady=5, side=LEFT)
        
        load19 = Image.open("images/test7.png") 
        resize_image19 = load19.resize((190, 190))
        render19 = ImageTk.PhotoImage(resize_image19)
        img19 = Checkbutton(border6, image=render19,
                                     variable=CheckbuttonValue20, onvalue=20, offvalue=0) 
        img19.pack(padx=30, pady=5, side=LEFT)
       
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img.destroy(), img1.destroy(), 
                                           img2.destroy(), img3.destroy(), 
                                           img4.destroy(), img5.destroy(), 
                                           img6.destroy(), img7.destroy(), 
                                           img8.destroy(), img9.destroy(), 
                                           img10.destroy(), img11.destroy(), 
                                           img12.destroy(), img13.destroy(), 
                                           img14.destroy(), img15.destroy(), 
                                           img16.destroy(), img17.destroy(), 
                                           img18.destroy(), img19.destroy(), 
                                           border3.destroy(), border4.destroy(), 
                                           border5.destroy(), border6.destroy(), 
                                           press7(t_start7)]
        
        window2.mainloop()

    def press5(t_start5):
        """
        Displays 10 pictures for 10 seconds.

        Input: t_start5 is the starting time
        """
        # to measure time
        t_end6 = time.time() - t_start5
 
        game2_label.config(text="Merke dir die Bilder. Zeit 10 Sekunden.")
        
        # to measure time
        t_start6 = time.time()
        
        next2_button.config(text="Weiter zur Lösungsseite.")
        
        window2.title("Spiel2a")
        
        # to frame pictures
        border1 = Frame(window2)
        border1.pack(side='top', padx='5', pady='1')
        
        # to load and visualize pictures
        load = Image.open("images/test1.png") 
        resize_image = load.resize((190, 190))
        render = ImageTk.PhotoImage(resize_image)
        img = Label(border1, image=render)
        img.pack(padx=30, pady=5, side=LEFT)
        
        load1 = Image.open("images/test3.png")
        resize_image1 = load1.resize((190, 190))
        render1 = ImageTk.PhotoImage(resize_image1)
        img1 = Label(border1, image=render1)
        img1.pack(padx=30, pady=5, side=LEFT)
        
        load2 = Image.open("images/test4.png") 
        resize_image2 = load2.resize((190, 190))
        render2 = ImageTk.PhotoImage(resize_image2)
        img2 = Label(border1, image=render2)
        img2.pack(padx=30, pady=5, side=LEFT)
        
        load3 = Image.open("images/test2.png") 
        resize_image3 = load3.resize((190, 190))
        render3 = ImageTk.PhotoImage(resize_image3)
        img3 = Label(border1, image=render3)
        img3.pack(padx=30, pady=5, side=LEFT)
        
        load4 = Image.open("images/test5.png") 
        resize_image4 = load4.resize((190, 190))
        render4 = ImageTk.PhotoImage(resize_image4)
        img4 = Label(border1, image=render4)
        img4.pack(padx=30, pady=5, side=LEFT)
        
        border2 = Frame(window2)
        border2.pack(side='top', padx='5', pady='1')
        
        load5 = Image.open("images/test6.png") 
        resize_image5 = load5.resize((190, 190))
        render5 = ImageTk.PhotoImage(resize_image5)
        img5 = Label(border2, image=render5)
        img5.pack(padx=30, pady=5, side=LEFT)
        
        load6 = Image.open("images/test7.png") 
        resize_image6 = load6.resize((190, 190))
        render6 = ImageTk.PhotoImage(resize_image6)
        img6 = Label(border2, image=render6)
        img6.pack(padx=30, pady=5, side=LEFT)
        
        load7 = Image.open("images/test8.png") 
        resize_image7 = load7.resize((190, 190))
        render7 = ImageTk.PhotoImage(resize_image7)
        img7 = Label(border2, image=render7)
        img7.pack(padx=30, pady=5, side=LEFT)
        
        load8 = Image.open("images/test9.png") 
        resize_image8 = load8.resize((190, 190))
        render8 = ImageTk.PhotoImage(resize_image8)
        img8 = Label(border2, image=render8)
        img8.pack(padx=30, pady=5, side=LEFT)
        
        load9 = Image.open("images/test.png")
        resize_image9 = load9.resize((190, 190))
        render9 = ImageTk.PhotoImage(resize_image9)
        img9 = Label(border2, image=render9)
        img9.pack(padx=30, pady=5, side=LEFT)
        
        # destroy all picutres after 10 seconds
        img.after(10000, img.destroy)
        img1.after(10000, img1.destroy)
        img2.after(10000, img2.destroy)
        img3.after(10000, img3.destroy)
        img4.after(10000, img4.destroy)
        img5.after(10000, img5.destroy)
        img6.after(10000, img6.destroy)
        img7.after(10000, img7.destroy)
        img8.after(10000, img8.destroy)
        img9.after(10000, img9.destroy)
        border1.after(10000, border1.destroy)
        border2.after(10000, border2.destroy)
        
        # destroy all picutres and pass time value
        next2_button['command'] = lambda: [img.destroy(), img1.destroy(), 
                                           img2.destroy(), img3.destroy(), 
                                           img4.destroy(), img5.destroy(), 
                                           img6.destroy(), img7.destroy(), 
                                           img8.destroy(), img9.destroy(), 
                                           border1.destroy(), border2.destroy(), 
                                           press6(t_start6)]
        window2.title("Spiel 2.1")
        window2.mainloop()
        
    # to measure time
    t_start5 = time.time() 
    
    next2_button = Button(window2, text="Beginne Spiel 2.1", command=lambda: press5(t_start5))

    game2_label.pack()
    
    next2_button.pack()
  
###########################################################
################### DEFINE FIRST WINDOW ###################
###########################################################

window = Tk()
window.title("Experiment")
window.geometry('650x500')

next_button = Button(window, text="Spiel 1", command=game1)
exit_button = Button(window, text="Spiel 2", command=game2)

next_label = Label(window, text="Leseverständnis")
exit_label = Label(window, text="Bildermerken")

# load Goethe Logo
goethe_load = Image.open("images/test71.png") 
goethe_resize_image = goethe_load.resize((525, 350))
goethe_render = ImageTk.PhotoImage(goethe_resize_image)
goethe_img = Label(window, image=goethe_render)
    
next_label.pack()
next_button.pack()

exit_label.pack()
exit_button.pack()
goethe_img.pack(padx=30, pady=15)

window.mainloop()

