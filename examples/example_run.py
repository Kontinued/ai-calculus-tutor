from tutor.graph import app

result = app.invoke({
    "question": "derivative of x^2",
    "student_level": "intermediate"
})

print(result["explanation"])
