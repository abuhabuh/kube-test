from flask import Flask, render_template, request

app = Flask(
  __name__,
  template_folder='',
  static_folder='')

app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/', methods=['GET'])
def handle_play():
  return 'hello world'


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=12046)

