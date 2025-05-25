# Schedule Scraper
This tool is designed to scrape the data from the official PUCP website. Specifically, it is focuse on the schedules, so it will be easier to manipulate the data in order to genate schedules for studentes with their own preferences. The reason for this tool is because as I was inspecting the website, it looks like the data is fetched in the server, so its not visible on the frontend in a comprenhensive file.

---

## Data Structure
The output data will be presented in a comprenhensive json data. However, in the future will be interesting to explore a reltaional data structure. 

---

### Structure of the raw data
The data is diplayed in tables in the PUCP website 14 columns (1 not displayed) and multiple rows inside an html document. 
The columns are the following:
- **Clave**: The unique code od the course.
- **Nombre del curso**: The extended name of the course.
- **Cr.**: The number of credits of the course. 
- **Tipo Hor.**: The type of the individual class: 
  - **Cla**: It means a usual class.
  - **Pra**: It means a graded assesment.
  - **Dir**: It means a directed assesment.
  - **Lab**: It means a laboratory class. 
  - **Exam**: It means a exam.

### Example of Raw Data

Below is an example of on row of the raw data extracted from the PUCP website:

```html
<tr>
    <td rowspan=6>CDR121</td>
    <td rowspan=6>CIENCIA, ÉTICA Y CRISTIANISMO</td>
    <td rowspan=6>3.5</td>
    <td>Cla</td>
    <td>0261 <a class="pucpLinkCeldaGris" href="#LEYENDA"></a></td>
    <td>&nbsp;</td>
    <td>60</td>
    <td>60</td>
    <td>67</td>
    <td>0</td>
    <td>Caviglia, A</td>
    <td>MAR 15:00-17:00 C Z214<br />JUE 15:00-16:00 C Z214</td>
    <td style="display:none">S&iacute;&nbsp;</td>
    <td>No</td>
</tr>
