from ControllerClass.ClassWebScraping import ControllerAPI;
import time as time


p1 = "//span[@class='d-table-cell v-align-middle lh-condensed pr-2']//strong"
p2 = "//span[@class='p-nickname vcard-username d-block']"

meuip = ControllerAPI("Meu IP", "https://github.com/lcrochaDEV/", p1)
meuip.varrerDados()