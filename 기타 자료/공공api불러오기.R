install.packages("httr") # HTTP통신을 위한 패키지 설치

library(httr)
GET('http://apis.data.go.kr/1390802/SoilEnviron/SoilExam/getSoilExam?serviceKey=서비스키&PNU_Code=4215034022100620003')


install.packages("XML")
library(XML)

url = "http://apis.data.go.kr/1390802/SoilEnviron/SoilExam"
auth_key = "C9isPJO3CKoK7UK894DKnDD1mvMwmXq0DcJAdqOac13fXCyVNoweotfGxW2qGKhRYeGAfu8wCTYDpgEADGjAxA%3D%3D"
# sample 제거
type = 'xml'
service = 'ListPublicReservationCulture'
startindex = '1'
endindex = '50'
api_url = paste(url, auth_key, type, service, startindex, endindex, sep = '/')
parsedXml <-xmlParse(api_url)




path = "gunwi1.xls"








