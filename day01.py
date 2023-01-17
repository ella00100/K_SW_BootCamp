subjects = { 'Operating System' : 'A+',
             '회로이론' : 'B+',
             '수치해석' : 'A0'
}
student = 'dungdung'
subject = 'Operating System'

#basic
print(student, '학생의' , subject, '과목 성적은', subjects[subject],'입니다')
#old style
print("%s 학생의 %s 과목 성적은 %s입니다" % (student,subject, subjects[subject]))
# format함수 modern sytle
print("{0} 학생의 {1} 과목 성적은 {2}입니다".format(student, subject, subjects[subject]))
#f string( vltra modern style)
print(f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]}입니다')