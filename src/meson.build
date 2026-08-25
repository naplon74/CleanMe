pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'clean_me'
gnome = import('gnome')

gnome.compile_resources('clean_me',
  'clean_me.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'clean_me.in',
  output: 'clean_me',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x'
)

clean_me_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'blur.py'
]

install_data(clean_me_sources, install_dir: moduledir)
