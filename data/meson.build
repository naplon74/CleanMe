desktop_file = i18n.merge_file(
        input: 'io.github.Naplon.CleanMe.desktop.in',
       output: 'io.github.Naplon.CleanMe.desktop',
         type: 'desktop',
       po_dir: '../po',
      install: true,
  install_dir: get_option('datadir') / 'applications'
)

desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils, args: [desktop_file])
endif

appstream_file = i18n.merge_file(
        input: 'io.github.Naplon.CleanMe.metainfo.xml.in',
       output: 'io.github.Naplon.CleanMe.metainfo.xml',
       po_dir: '../po',
      install: true,
  install_dir: get_option('datadir') / 'metainfo'
)

appstreamcli = find_program('appstreamcli', required: false, disabler: true)
test('Validate appstream file', appstreamcli,
     args: ['validate', '--no-net', '--explain', appstream_file])

install_data('io.github.Naplon.CleanMe.gschema.xml',
  install_dir: get_option('datadir') / 'glib-2.0' / 'schemas'
)

compile_schemas = find_program('glib-compile-schemas', required: false, disabler: true)
test('Validate schema file',
     compile_schemas,
     args: ['--strict', '--dry-run', meson.current_source_dir()])


service_conf = configuration_data()
service_conf.set('bindir', get_option('prefix') / get_option('bindir'))
configure_file(
  input: 'io.github.Naplon.CleanMe.service.in',
  output: 'io.github.Naplon.CleanMe.service',
  configuration: service_conf,
  install_dir: get_option('datadir') / 'dbus-1' / 'services'
)

subdir('icons')

# Install screenshots directory (if you add screenshots in data/screenshots/)
# Install individual screenshot files into share/metainfo/screenshots so
# AppStream can find them using the relative paths referenced in the metainfo
# file.
  screenshots_files = []
  comp_name = 'io.github.Naplon.CleanMe'
  screenshots_subdir = 'screenshots/' + comp_name
  if meson.is_subproject() == false
    # Only collect screenshots when building from the source tree
    screenshots_files = [
      screenshots_subdir + '/1.png',
      screenshots_subdir + '/2.png',
    ]
  endif
  if screenshots_files.length() > 0
    install_data(screenshots_files, install_dir: get_option('datadir') / 'metainfo' / 'screenshots' / comp_name)
  else
    # Ensure an empty screenshots directory is present for packaging tools
    install_emptydir(get_option('datadir') / 'metainfo' / 'screenshots' / comp_name)
  endif
