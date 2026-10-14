import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')# leemos el csv, gracias al módulo línea 2
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: float(x['World Population Percentage']), data))
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')
  print(country)

  # 1. Buscamos los datos del pais que ingreso el usuario
  result = utils.population_by_country(data, country)

  if len(result) > 0:
      country_data = result[0]
      print(country)
      # 2. Extraemos las etiquetas (años) y los valores (población)
      labels, values = utils.get_population(country_data)
      # 3. Llamamos a la función para generar el gráfico de barras
      charts.generate_bar_chart(country_data['Country'], labels, values)

if __name__ == '__main__':
  run()