import webapp2
class Temp(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('''
<h2>Celcius to Farenheit</h2>
<form method="post">
    Enter temp: <input name="c">
    <input type="submit" value="Convert">
</form>
''')

    def post(self):
        c=float(self.request.get('c'))
        f=(c*9/5)+32
        self.response.out.write('<h3>Farenheit = %.2f</h3>'%f)
        self.response.out.write('<a href="/">Back</a>')
app=webapp2.WSGIApplication([('/',Temp)],debug=True)

