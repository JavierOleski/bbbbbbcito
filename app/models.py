from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


class Ficha(models.Model):
    Si = 'Sí'
    No = 'No'
    opcion_binaria = [(Si, 'Sí'), (No, 'No')]

    Juanete = 'Juanete'
    Dedo_martillo = 'Dedo martillo'
    Dedo_garra = 'Dedo_garra'
    Guanetillo = 'Guanetillo'
    opcion_antepie = [(Juanete, 'Juanete'), (Dedo_martillo, 'Dedo martillo'), (Dedo_garra, 'Dedo garra'),
                      (Guanetillo, 'Guanetillo')]

    Plano = 'Plano'
    Cavo = 'Cavo'
    opcion_mediopie = [(Plano, 'Plano'), (Cavo, 'Cavo')]

    Izquierdo = 'Izquierdo'
    Derecho = 'Derecho'
    Ambos = 'Ambos'
    opcion_lado_afectado = [(Izquierdo, 'Izquierdo'), (Derecho, 'Derecho'), (Ambos, 'Ambos')]

    Uno = '1'
    Dos = '2'
    Tres = '3'
    Mas = 'Más'
    opcion_numerica = [(Uno, '1'), (Dos, '2'), (Tres, '3'), (Mas, 'Más')]

    Plantar = 'Plantar'
    Dorsal = 'Dorsal'
    Ambos = 'Ambos'
    opcion_localizacion_1 = [(Plantar, 'Plantar'), (Dorsal, 'Dorsal'), (Ambos, 'Ambos')]

    Antepie = 'Antepie'
    Mediopie = 'Mediopie'
    Retropie = 'Retropie'
    opcion_localizacion_2 = [(Antepie, 'Antepie'), (Mediopie, 'Mediopie'), (Retropie, 'Retropie')]

    Hallux = 'Hallux'
    Dedos_menores = 'Dedos menores'
    Metatarsiano = 'Metatarsiano'
    CLM = 'CLM'
    CLL = 'CLL'
    Talon = 'Talon'
    Dorso_mediopie = 'Dorso mediopie'
    opcion_localizacion_3 = [(Hallux, 'Hallux'), (Dedos_menores, 'Dedos menores'), (Metatarsiano, 'Metatarsiano'),
                             (CLM, 'CLM'), (CLL, 'CLL'), (Talon, 'Talon'), (Dorso_mediopie, 'Dorso mediopie')]

    Escaso = 'Escaso'
    Regular = 'Regular'
    Abundante = 'Abundante'
    opcion_secrecion1 = [(Escaso, 'Escaso'), (Regular, 'Regular'), (Abundante, 'Abundante')]

    Seroso = 'Seroso'
    Sanguinoliento = 'Sanguinoliento'
    Purulento = 'Purulento'
    opcion_secrecion2 = [(Seroso, 'Seroso'), (Sanguinoliento, 'Sanguinoliento'), (Purulento, 'Purulento')]

    Negro = 'Negro'
    Amarillo = 'Amarillo'
    Rojo = 'Rojo'
    opcion_color1 = [(Negro, 'Negro'), (Amarillo, 'Amarillo'), (Rojo, 'Rojo')]

    Perilesional = 'Perilesional'
    Intralesional = 'Intralesional'
    opcion_zona_contaminacion = [(Perilesional, 'Perilesional'), (Intralesional, 'Intralesional')]

    Nombre = models.CharField(max_length=40)
    DNI = models.DecimalField(decimal_places=0, max_digits=8, null=True)
    Edad = models.DecimalField(decimal_places=0, max_digits=3, null=True)
    Tiempo_de_enfermedad = models.DecimalField(default=False, decimal_places=0, max_digits=2)

    # Complicaciones
    Retinopatia = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Netropatia = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Hipoglicemia = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Coma_diabetico = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Accidente_cerebro_vascular = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Infarto_miocardio = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Hipertension = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')

    # Sintomas Perifericos
    Adormecimiento_o_dolor = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Claudicacion = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Callos_o_deformidad = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')

    # Evaluacion neurológica periférica
    Sensibilidad_tactil_alterada = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Sensibilidad_vibratoria_alterada = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Sensibilidad_neurovegetativa_alterada = models.ImageField(upload_to='SensibilidadNeurovegetativaAlterada/%Y/%m/%d',
                                                              default='Sí')

    # Evaluacion arterial periférica
    # Macrovascular
    Presion_arterial_tobillo = models.DecimalField(default=False, decimal_places=0, max_digits=2)
    Presion_arterial_brazo = models.DecimalField(default=False, decimal_places=0, max_digits=2)
    # Microvascular
    Recuperacion_termica_a_0_minutos = models.ImageField(upload_to='RecuperacionTermicaACeroMinutos/%Y/%m/%d',
                                                         default='Sí')
    Recuperacion_termica_a_4_minutos = models.ImageField(upload_to='RecuperacionTermicaACuatroMinutos/%Y/%m/%d',
                                                         default='Sí')
    Recuperacion_termica_a_8_minutos = models.ImageField(upload_to='RecuperacionTermicaAOchoMinutos/%Y/%m/%d',
                                                         default='Sí')

    # Evaluación músculo esquelética pie
    Presion_plantar_alta = models.ImageField(upload_to='PresionPlantarAlta/%Y/%m/%d', default='Sí')
    Callos = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Localización = models.CharField(max_length=40)
    Deformidad_del_antepie = models.CharField(max_length=2, choices=opcion_binaria, default='Sí')
    Tipo_deformidad_del_antepie = models.CharField(max_length=15, choices=opcion_antepie, default='Juanete')
    Deformidad_del_mediopie = models.CharField(max_length=15, choices=opcion_mediopie, default='Plano')

    # Evaluación de la úlcera diabética no infectada (neurovascular)
    Lado_afectado = models.CharField(max_length=10, choices=opcion_lado_afectado, default='Izquierdo')
    Numero = models.CharField(max_length=3, choices=opcion_numerica, default='1')
    Localizacion_1 = models.CharField(max_length=15, choices=opcion_localizacion_1, default='Plantar')
    Localizacion_2 = models.CharField(max_length=15, choices=opcion_localizacion_2, default='Antepie')
    Localizacion_3 = models.CharField(max_length=15, choices=opcion_localizacion_3, default='Hallux')
    Secrecion_1 = models.CharField(max_length=15, choices=opcion_secrecion1, default='Escaso')
    Secrecion_2 = models.CharField(max_length=15, choices=opcion_secrecion2, default='Seroso')
    Color_1 = models.CharField(max_length=15, choices=opcion_color1, default='Negro')
    Color_predominante = models.CharField(max_length=10)
    Dimensiones_largo_maximo = models.DecimalField(default=False, decimal_places=0, max_digits=2)
    Dimensiones_ancho_maximo = models.DecimalField(default=False, decimal_places=0, max_digits=2)
    Area_de_la_ulcera = models.DecimalField(default=False, decimal_places=0, max_digits=2)
    Fotografia_convencional = models.ImageField(upload_to='AreaDeLaUlcera/%Y/%m/%d', default='Sí')
    Zona_de_contaminacion_bacterial = models.CharField(max_length=15, choices=opcion_zona_contaminacion,
                                                       default='Perilesional')
    Fotografia_autoluminiscente = models.ImageField(upload_to='ZonaDeContaminacion_Bacterial/%Y/%m/%d', default='Sí')

    # Evaluación de la úlcera infectada
    # Grado leve
    Edema_local = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Induracion = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Celulitis_menor_de_2_cm = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Sensibilidad_o_dolor = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Secrecion_purulenta = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Diferencial_termico_alterado = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Adjuntar_imagen_termica = models.ImageField(upload_to='DiferencialTermicoAlterado/%Y/%m/%d', default='Sí')
    # Grado moderado
    Celulitis_mayor_de_2_cm = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Absceso = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Fascitis = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Artritis_septica = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Osteomielitis = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    # Grado severo
    Temperatura_mayor_a_38_o_menor_a_36 = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Frecuencia_cardiaca_mayor_a_90_por_minuto = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Frecuencia_respiratoria_mayor_a_32_por_minuto = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')
    Presion_parcial_de_dioxido_de_carbono_menor_de_35_mm_Hg = models.CharField(max_length=3, choices=opcion_binaria,
                                                                               default='Sí')
    Recuento_celular_mayor_a_12000_o_menor_a_4000 = models.CharField(max_length=3, choices=opcion_binaria, default='Sí')


    def __str__(self):
        return self.Nombre


# def pacientes(request):
#     return render(request, 'pacientes.html')
#
# def ficha_medica(request):
#     return render(request, 'ficha_medica.html')
