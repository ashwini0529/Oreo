from example_apps.basic_app import create_app
<<<<<<< HEAD

app = create_app()

app.run(port=5001, debug=True)
=======
import os

app = create_app()

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port= port)
>>>>>>> 0b3d1889f172757bcd9df1076002ef012fb747f6

