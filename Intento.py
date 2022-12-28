from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
print(type(bot))
articulo='''
João de Mascarenhas:

Biografía
Cuarto hijo del D. Fernando de Mascarenhas (c 1610-1651) (1er Conde da Torre y Gobernador General del Estado del Brasil), y de Doña María de Noronha (c 1610 -.?).
Desempeñó el cargo de mayordomo mayor (Mordomo-mor) en Faro. Séptimo administrador de las heredades (morgadios) de Goucharia y Chantas, y el primero de la heredad de Torre das Vargens. A la muerte de su hermano mayor, Manuel Mascarenhas, se convirtió en el heredero de la casa y señor de las heredades de Coculim y Verodá, en la India portuguesa. Además, comendador de las siguientes órdenes: Ordem de Cristo de Nossa Senhora da Conceição do Rosmaninhal, Santiago da Fonte Arcada, São Nicolau de Carrazedo, São João de Castelões, São Martinho de Cambres y de São Martinho de Pindo. También fue patrón de los Monasterios de Nossa Senhora da Conceição da Torre das Vargens y de São Domingos da Serra.
Chambelán del Infante D. Pedro. Por este cargo quedó involucrado en las luchas palaciegas que llevaron a la abdicación de Alfonso VI y el ascenso de Pedro II al trono. Este rey premió a João Mascarenhas, en Carta de 7 de enero de 1670, con el título de Primer Marqués de Fronteira, uno de los más importantes de Portugal. También ocupó los cargos de 48 Vedor da Facenda o Hacienda (nombrado el 12 de octubre de 1676), y consejero de los Consejos de Estado y de Guerra. Así mismo, fue familiar del Santo Oficio (trabajaba para esa institución).
En el contexto de la Guerra de la Restauración, ejerció de Maestre de Campo en la provincia de Alentejo (1657), General Maestre de Campo en la provincia de Minho y General de Caballería en la campaña de 1662 del Alentejo. Fue gobernador de la plaza-fuerte de Campo Maior. Participó en el sitio de Badajoz, en el asalto a Valencia de Alcántara, la recuperación de la plaza-fuerte de Mourao, en la batalla de las Líneas de Elvas (1659), la batalla de Ameixial (1663) y la batalla de Montes Claros (1665).
Tras la paz de 1668, fue nombrado General Maestre de Campo en la provincia de Estremadura.

Basado en lo anterior generar 5 preguntas de opcion multiple y sus respuestas correctas.
'''
response = bot.ask(articulo)
print(response)  # prints the response from chatGPT