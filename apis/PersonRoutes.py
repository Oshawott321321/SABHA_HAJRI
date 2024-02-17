from io import BytesIO
from flask_restx import Namespace, Resource, reqparse
from flask import render_template,make_response,request,send_file ,redirect ,url_for
from models import *
from utils.db import db
from datetime import date
import xlsxwriter
import werkzeug
import csv

api = Namespace('Data', description='')

@api.route('/abcd')
class Form(Resource):
    def get(self):
        data = PersonModel.query.all()
        today_date = date.today().__str__()
        newdata = []
        for i in data:
            curObj = {
                "id":i.id,
                "name":i.name,
                "role_no":i.role_no,
                "male":0,
                "female":0
            }
            t = i.atten
            flag = False
            for j in t:
                # print( i, j )
                if j.onlydate==today_date:
                    curObj['male'] = j.maleCount
                    curObj['female'] = j.femaleCount
                    print(j.maleCount, j.femaleCount)
                    break
            if flag==False:
                newdata.append(curObj)
                    
        return make_response(render_template('form.html',data=newdata,date=date.today().__str__()))

    def post(self):
        print("in Post")
        data = PersonModel.query.all()
        return make_response(render_template('form.html',data=data))
    

person_parser = reqparse.RequestParser()
person_parser.add_argument('name',type=str)
person_parser.add_argument('id',type=int)
person_parser.add_argument('male',type=int)
person_parser.add_argument('female',type=int)

@api.route('/person')
class Person(Resource):
    def get(self):
        return {}

    def post(self):
        d = person_parser.parse_args()
        print(d)
        if not d['id']:
            return {}
        todaydate = date.today().__str__()
        doesExist = AttendanceModel.query.filter_by(onlydate = todaydate).filter_by(person=d['id']).first()
        if doesExist is None:
            a = AttendanceModel()
            a.person = d['id']
            a.maleCount =d['male']
            a.femaleCount= d['female']
            a.__save__(db)
        else:
            a = doesExist
            a.maleCount =d['male']
            a.femaleCount= d['female']
            db.session.add(a)
            db.session.commit()

        print(a)
        return { 'saved':'saved'}

register_parser = reqparse.RequestParser()
register_parser.add_argument('name',type=str)
register_parser.add_argument('roll_no',type=int)
@api.route('/register')
class Person(Resource):
    def get(self):
        return make_response(render_template('personRegister.html'))

    def post(self):
        d = register_parser.parse_args()
        print(d)
        if(PersonModel.__save__(db,d['name'],d['roll_no'])) is None:
            return {"saved":"not"}
        return { 'saved':'saved'}

getData_parser = reqparse.RequestParser()
getData_parser.add_argument('date',type=str)

@api.route('/getData')
class GetData(Resource):
    def get(self):
        return make_response(render_template('getData.html'))
    def post(self):
        rd = getData_parser.parse_args()
        print(rd)
        buffer = BytesIO()
        workbook = xlsxwriter.Workbook(buffer)
        worksheet = workbook.add_worksheet()
        i =1
        j =0
        d = AttendanceModel.query.filter_by(onlydate=rd['date']).all()
        male_cnt=0
        female_cnt=0
        worksheet.write(0,0,"No")
        worksheet.write(0,1,"Date")
        worksheet.write(0,2,"personId")
        worksheet.write(0,3,"Name")
        worksheet.write(0,4,"Male")
        worksheet.write(0,5,"Female")
        for itr in d:
            worksheet.write(i,j,itr.id)
            worksheet.write(i,j+1,itr.onlydate)
            # for jtr in itr.personBack:
            jtr=itr.personBack
            worksheet.write(i,j+2,jtr.id)
            worksheet.write(i,j+3,jtr.name)
            worksheet.write(i,j+4,itr.maleCount)
            worksheet.write(i,j+5,itr.femaleCount)
            male_cnt+=itr.maleCount
            female_cnt+=itr.femaleCount
            i+=1
        worksheet.write(i+3,0,"Male :"+str(male_cnt))
        worksheet.write(i+4,0,"Female :"+str(female_cnt))
        workbook.close()
        buffer.seek(0)
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        downloaded_filename=f"Attendance_Data_{rd['date']}.xlsx"
        return send_file(buffer,as_attachment=True,download_name=downloaded_filename,mimetype=mimetype)

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('attachment', type=werkzeug.datastructures.FileStorage, location='files')
@api.route('/upload')
class Upload(Resource):
    def get(self):
        return make_response(render_template('upload.html'))

    def post(self):
        d = upload_parser.parse_args()
        print(d)
        f = d.get('attachment')
        print(f)
        print(f.filename, f.mimetype)
        f.save('instance/'+f.filename)
        resp = {
            "could not add":[],
            "added":[]
        }
        try:
            with open('instance/'+f.filename, mode ='r')as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    gender = 'male' if len(lines)>2 and lines[2]=="M" else 'female'
                    result = PersonModel.__save__(db,lines[1], int(lines[0]) )
                    if result is None:
                        resp['could not add'].append(lines[1])
                    else:
                        resp['added'].append(lines[1])
                    # resp.append(lines)
                    # doesExist = PersonModel.query.filter_by(name=lines[1]).first()
                    # if doesExist is None:
                    #     PersonModel.__save__(db,lines[1],'male' if lines[2]=="M" else 'female' )
                    #     resp['added'].append(lines[1])
                    # else:
                    #     print(f'${lines[1]} already Exist')
                    #     resp['exist'].append(lines[1])
        except Exception as e:
            print(e.__str__(),e)
            return { "ERrpr":"some ereror"}
        return resp
        return redirect(url_for('Data_upload'))    