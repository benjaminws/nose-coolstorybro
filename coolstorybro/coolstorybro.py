# -*- encoding: utf-8 -*-

import inspect
import os

from nose.case import MethodTestCase
from nose.plugins import Plugin
from unittest import TestResult, _TextTestResult

CHUCK_TESTA = """
                                        =II7$Z$$$$$?
                                      ?7$ZOIIZDDDD8O$
                                     I$ZZOO$Z$$7II77$$
                                    7ZOO$777O??II7$$Z7$
                                    $II777IIIZ8NMMNNDO$Z
                                   Z$$Z7+78MMMNNNNMMNNDO
                                  8D$OI7DNNNNDDDDDNNNNNZ
                                   8Z$DNNNDDO?~~~==?DDNZ
                                   7$NNNNN$?==~=ZDD88DO+
                                    ONDD8DDDNN7IDNNNOOI?
                                    +DO8D8NDD8+~IDDDDOZ~
                                    ?OO$$DDDOI?:+++7Z8?=
                                     OOI8OZ+=IOI$+=+?+?=
                                      OZ8$?+=~=$+=~===I
   D                                    O7?=+IZ888O+++7
 ODDO                                   ZZI+IIIIII??$Z$
NNDD8                                78D8OOOZ???+~~=7OO
NNDDD8                        ???III?8DND888OI=====$8O+~IOIO
NNNDD8                     ??IIIIIIIIII$8DDD88ZI?IODO$$$II7III
ZONDDDD                 7IIIIIIIIIIIIII77$ZNNNNNNMNNZ777777IIIII
 ZODDDD8             ODI77I7IIIIIIIIIII7I7$ONNMMMMN$77$ZZ$77IIIIII
 ZD788888          D8IIII777IIIIIIIIIIIIIII7$$O8Z$777IIIIIIIIIIIIII?
 8D=?+8Z88       O77II77I777IIIIIIIIIIIIIII7777777777IIIIIIIIIIIIIIII
 $D8:==$=IZDD 7777777777777IIIIIIIIIIIIIIIIII7I77777IIIIIIIIIIIIIIIIII?
  D8+~~====77777777777777777IIIIIIIIIIIIIIIIIIIIIIIII~,=I+:=III7IIIIIIII
   OI++====77$$Z7777$7777777IIIIIIIIIIIIIIIIIIIIIIIIIII+.~:=:I7IIIIIIIII
    8I++===$$7Z$Z8Z$$7777777IIIIIIIIIIIIIIIIIIIIIIIII?+==:+I+IIIIIIIIIII7
     $I?+++7$$ZZ$$$ZZ7777777IIIIIIIIIIIIIIIIIIIIIIII~~~???I~=7II777II77I?
     8$7?+=7$$ZZZZZ$$$777777IIIIIIIIIIIIIIIIIIIIIII::?==~~+~I7I777777III?I
      8Z$7?7Z$Z$ZZZ$$$7777777IIIIIIIIIIII777IIIIIIIII?I?=+7II7I7$7$IIIII??
       OOZ$O?$Z$ZOZZZ$777$$7777777777777777777IIIIIIIIIIIII777$7$$7II???III
           MD?Z$ZZDOZ$$77$77$77777777I7777777777IIIIIIIIII77$$$7$7I7???III?
                OZ$DZZZ$$7$$$$7777777III77II77777$7777777II7$$$7777I??I????$
                   ODZZ$7$$7$$7777777IIIIIIIII777ZOZ$$77$DZ777$$Z7IIII?????I
                     O$$$$777$77777I77IIIIIIIII7$777ZDZNZ7NZ777$Z7III???????
                     OZ$$$77$$77777I77IIIIIII77ZIIII$ODZNO7D$77$O7IIIII?????I
                      Z$$7777777777II7IIII77IIIII77777777O87O77OO777IIIIII???
                      Z$77777777777IIIIIIII7IIIIIIIIII77777O$Z8NZ$$777III??I?
                      Z$77777777777IIIIIIIII77IIIIIIIII777I7Z$M$Z77$$7IIIIIII7$
                      =77777777777IIIIIIIIIII77IIIII7777777I7$ZM87III777$ODMMMD
                      $:I7777777777IIIIIIIIII7$$IIIIIII7777II7$Z$$O8+~==+7NMMN
                      Z7+777777777777IIIIIIIIII777IIIIIIIIIII77ONZ+====+?Z8
                      $77II777777777777777IIII77I77IIIIIII77777ZD+=~=++?77
                      $7777=7777777777777777III777777IIII7777777+====++I7$
                      $777II:7777777777777777IIIIII777IIII777III=~===+I7$Z
                      $877777I777777777$7$77777777$ZOO8O7IIIIII+=====+7$O
                      777Z$777$=77$$77777$$$777$$$7I777ZNDZ7II?==~=+?7$
                     Z77777877$$:77$7777777$$77777$$7777$8MNZI===++??I
                     Z777777$8Z$7I?777$$$$$$$$$$777$$$$$Z$ZOI+===??I7
                     77I777777$$Z$7:$$$$$$$$$$$$777$$$$$77I+===+?IIZ
                                                                          8
                                                                      OII?MM
                                                                 OO   II??OM
                                                             Z7III?MM  II?7MM
                                                         O7III???IOOM   I?+MM
                                                     ZIII????ZMMMM       I+MM
                                                     7II??DMMM OI M      ZOMMM
                                           $7IIIIIIM  $II?$OIIII?ZM       II?OM
                                       Z7III????II??MM II?II???ZMMMM O   OI??ZMM
                                     III???I8MMM8I?+DM OII??MMMM  O7II8M   ZMMM
                                     OII??MM    $I+?MM  II??OMOIIII???IMM
                          O7IIIIZ     II??ZMOIII??$MM   OII?III???ZNMMMM
                       OIII????I?I?D   II??I???ZMMMM     I????ZMMMM
                     ZII??$NMM8III??8M $II?7MMMM         OOMMMM
              O7    $I??OMMM    OII??MM II??8M
            II??MM 8II?$MM       II?+MM OII?IMM
     O      OII?ZM OII?ZMM      OII?7MM  I??I8M
7OIIII7M     $I??MM II??8M     ZII??MM     MMM
 III??III?O   II?IM OII??IIIIIII??OMM
 ZI??IIIIIII?ZZI??8M 8IIIII????IMMMM
  II??MM$IIIIIII???MM   MD8DMMMMM
  OI??8M   8I?III??8M
   II??MM     O7I?IOMM
   OII?OM        MMM
    7I??NM
    Z?OMMMM
      M
"""

FUUU = """
                          ,DNMM ,,.M. .,MD:.
                       MM,,.,.       ,M M..M.
                 . NM           .:M  NMN,    N.
                 ,M:            M.M,M.        M.
                DM              NDNM           M,.
               M                MD.            .MM
       :...NNMN                MMNMN. ,MM8. M.   MM.
       .:..,MMMMMM.           M,MNM. .N..    MN .M N.
           .    ..MM.N.       MMMM. .D:.   N, NM..M:.
       M,.M.        M.        M M  M       M . .M.,MM
       NMM      .... D,       ,MM,,.      .NMMMM.N..M
       M .     NN    MMM,     MNM,M,              M .N,
      MM     M          M        .M.               M..M,
   .M.,M    M,.        ,M M.       N.              M .MM:
    M.      M  N         ...        N              M   ,N
   .M.M.   .   M.         M          MM,          N.   M:M
   .M       M ...        M,   MN.,MNMN,.MNM     NM.     MM
   .MM      N          .M   MM.   M.,,..M.,             M
   .MM       .        ,M  .   M.  M,MM   .,M:,MM,        ,
   .MM      .N       N   N..  :MMMN.         ..M.M.     .M
   .MM.        MMMMMM  .. .M,..M                  M.     MM.
   .MM                  M  ,,MMM                   M.    :M.
   .MM                  M M.                       .N    .N,
   .MM                 .M..             MMM         .M.  .N,
   .M D                .N          ... .    M.  ...  M.  .M
     .M                M.       .M .,  .   ,, .M  MM.M.  .M
     ,D                N.       M .        M,, M   . M.  .M
     M,M              ,M,      .M     .MMM. .  M    M .  .MM
     M.M              M        .     N   MN .DMMMMM.      MM
     ,M. .            M         :, ..M    .M,.            MM
      .ND,           M,       ,M,,,...  MM,              .M,
         ..         ,M .,  .,.M     M,N.                .MM.
        ,M.:        M,.MN:.M.M.   ..M.                  MM
        ,...        M M ,   M..,.M ,                    M
         M M,        ..,MNMM,.M:.                      MM
        ,M   MM..                                    ,.M.
          M     MM .                                 .M
          ,M     ,,:                                 ,M
"""

TROLL = """
                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                 MMMMMMM      :MMMMM          MM            MM
              MMM                    .MMMMMM.      M         MMM
            MM                                   MM   M        MM
          MM         MMMMMN            .        ,M   M          MM
         MM       M                   M             M  M   Z     M
         MM      M          M         =               M          MM
         M                               MMMMMMMMMMM              MM
       MMM        .MMMMMMMN            MMM   MMMMMMMMM             MMM
      MM   NMMMMMOMMMMMMMMMMM        MMM   MMMMMMMMMMMM   M    :7+  MMM
     MM M                MMMMMMM      MMMMMM   M            .MMMM    M MM
    MM   M                  MM                 .MM       MMMM   MMM   8 MM
    MMM = MMMMMMMM  .M      MM                    MMMMMMM    M    .MM  ? MM
    MM. M       MMMMM      MM                               MMM    MM  M  M
    MMM M     M         ,MM           MMMM M             MMMM MMM   M  8  M
    MM       MMM       MMMM              MM          MMMM.   .MM.  MM    MM
     MM .M  MMMM    M    MMM      MMMMM MM8     .MMMMMM      MM    M8 .  MM
      MM    MMMMMM         MMMMM           MMMMMM    MM   MMMM       M  MM
       M    MMM MMMMMM               MMMMMMMM       MMMMMMMMM         MMM
       MM   MMM MM  MMMMMMMMMMMMMMMMMN     MN    OMMMMMM  MM         MM
       MM   MMM MM  MM     MM     M        MMMMMMMMMMMM  MM         MM
       MM   MMMMMMMMMM     MM     M    .MMMMMMMMM    MM MM         MM
       MM   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM        MM.         MM
       MM   MMMMMMMMMMMMMMMMMMMMMMMMMMM.    MM      MMM          MM
       MM    M.MM MMMMMMMMMMMMMN   MM        MM   MMM           MM
       MM    MM+M :M  MM    MM     MM        MMMMM.           MMM
       MM     .MMM MM  MM   MM     MM      MMMMM     M   M  MMM
       MM        +MMMMMMMMMMMMMMMMMMMMMMMMM      MM   M   MMM
       MM                                     M    M   MMMM
       M        M                         M    M    MMMM
       M    M      MM         .$MMMMMN   .MM     MMMM
       M      M                  .MM.        MMMM
       MM                                 MMMM
        MM                            MMMMM
         MMM                   ,MMMMMMM
           MMMMM.      ~MMMMMMMM
"""


class CoolStoryBro(Exception):

    def __init__(self, tl_dr=None, fu=None):
        self.tl_dr = tl_dr
        self.fu = fu

    def __str__(self):
        if self.tl_dr:
            return self.tl_dr
        return FUUU if self.fu else TROLL


class ChuckTesta(Exception):

    def __init__(self, tl_dr=None, fu=None):
        self.tl_dr = tl_dr
        self.fu = fu

    def __str__(self):
        if self.tl_dr:
            return self.tl_dr
        return CHUCK_TESTA


class CoolStoryBroPlugin(Plugin):

    name = 'coolstorybro'
    enabled = True

    def options(self, parser, env=os.environ):
        parser.add_option('--tl-dr', action='store_true')
        parser.add_option('--fu', action='store_true')
        parser.add_option('--chuck-testa', action='store_true')
        super(CoolStoryBroPlugin, self).options(parser, env=env)

    def configure(self, options, config):
        super(CoolStoryBroPlugin, self).configure(options, config)
        self.config = config
        if not self.enabled:
            return

        self.tl_dr = options.tl_dr or None
        self.fu = options.fu or None
        self.chuck_testa = options.chuck_testa or None

    def startTest(self, test):
        if isinstance(test, MethodTestCase):
            source = inspect.getsourcelines(test.test)
            test_length = len(source[0])
            exception = ChuckTesta if self.chuck_testa else CoolStoryBro
            if test_length > 8:
                if self.tl_dr:
                    raise exception("TL;DR: %d lines" % test_length)
                raise exception(fu=self.fu)
        pass

    def prepareTestRunner(self, runner):
        self.runner = runner

    def setOutputStream(self, stream):
        self.stream = stream
