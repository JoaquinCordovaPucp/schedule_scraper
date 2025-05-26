import json
from bs4 import BeautifulSoup

with open('rawdata.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
raw_rows = soup.find_all('tr')
rows = raw_rows[6:len(raw_rows)-22]

courses = []
current_course = None

for row in rows: 
    
    cells = row.find_all("td")

    if "rownspan" in cells.attrs:
        courses.append(current_course)
        current_course = {
            "codigo": cells[0].text.strip(),
            "nombre": cells[1].text.strip(),
            "creditos": float(cells[2].text.strip()),
            "horarios": []
        }
        horario = {
          "tipo": cells[3].text.strip(),
          "clave": cells[4].text.strip(),
          "clave_asociada": cells[5].text.strip(),
          "vacantes": cells[6].text.strip(),
          "vac_unid": cells[7].text.strip(),
          "matriculados": cells[8].text.strip(),
          "profesor": cells[9].text.strip(),
          "sesiones": []
          }
        
        sesiones: [
            
        ]

