# -*- coding: UTF-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
import store
import analisis

class Ventana(object):
    def __init__(self):
        self.final_method = None
        self.Store = store.Store()
        self.Sensor = analisis.Sensor()
        self.ciclo = False
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Admin Sistema de riego")
        window.connect("destroy", self.on_quit)

        vbox = gtk.VBox(False, 5)

        #Entry plant name
        self.label_plant_name = gtk.Label("Planta")
        self.entry_plant_name = gtk.Entry()
        self.entry_plant_name.connect("activate", self.on_button1_clicked)

        #Entry plant type
        self.label_plant_type = gtk.Label("Tipo")
        self.entry_plant_type = gtk.Entry()

        #Combobox to irrigation method
        self.label_irrigation_method = gtk.Label("Metodo de riego")

        irrigation_method_combo = gtk.combo_box_new_text()
        irrigation_method_combo.append_text('Aspersión')
        irrigation_method_combo.append_text('Goteo')
        irrigation_method_combo.append_text('Inundación')

        irrigation_method_combo.connect("changed", self.handle_combobox)
        irrigation_method_combo.set_active(0)

        #Data Send Button
        button = gtk.Button(stock="Enviar")
        button.connect("clicked", self.on_button1_clicked)


        button_start = gtk.Button(stock="Iniciar Ciclo")
        button_start.connect("clicked", self.button_action_start_stop)




        #pack widgets
        vbox.add(self.label_plant_name)
        vbox.pack_start(self.entry_plant_name, True, True, 0)

        vbox.add(self.label_plant_type)
        vbox.pack_start(self.entry_plant_type, True, True, 0)

        vbox.add(self.label_irrigation_method)
        vbox.add(irrigation_method_combo)

        # Finalmente en la tercer fila agregamos el boton.
        vbox.pack_start(button, False, False, 0)

        vbox.pack_start(button_start, False, False, 0)

        # Ahora agregamos la caja vertical a la ventana y luego se muestra
        # la caja (y todo lo que contiene) en la ventana principal.
        window.add(vbox)
        window.show_all()

    def button_action_start_stop(self, button):
        if self.ciclo == False:
            #self.Sensor.start()
            self.ciclo = True
            button.set_label("Detener Ciclo")
        elif self.ciclo == True:
            #self.sensor.stop()
            self.ciclo = False
            button.set_label("Iniciar Ciclo")

    # Primero definamos el método "on_button1_clicked"
    def on_button1_clicked(self, widget):
        # Primero obtenemos el texto que se escriba en la entrada de texto
        plant_name = self.entry_plant_name.get_text()
        plant_type = self.entry_plant_type.get_text()
        irrigation_method = self.final_method

        if plant_type is "" or plant_name is "":
            dialog = gtk.Dialog("Error")
            dialog_label = gtk.Label("Por favor llene todas las entradas antes de enviar los datos.")
            dialog.vbox.add(dialog_label)
            dialog.show_all()
        else:
            self.Store.set_plant(plant_name, irrigation_method)
            plant_name = self.entry_plant_name.set_text("")
            plant_type = self.entry_plant_type.set_text("")

    def handle_combobox(self, combo):
        tree_iter = combo.get_active()
        if tree_iter is not None:
            model = combo.get_model()
            method = model[tree_iter][0]
            print("Selected: method=%s" % method)

            if method == "Goteo":
                self.final_method = "goteo"

            elif method == "Aspersión":
                self.final_method = "aspersion"

            elif method == "Inundación":
                self.final_method = "inundacion"
        return


    # Ahora se define el método "on_quit" que destruye la aplicación
    def on_quit(self, widget):
        gtk.main_quit()
