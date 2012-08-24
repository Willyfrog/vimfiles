==Pasos para instalar==
# clonar el repositorio
   git clone git@github.com:Willyfrog/vimfiles.git
# inicializar y descargar submodulos
   git submodule init
   git submodule update
# enlazar ficheros
   ln -s ~/vimfiles/vim ~/.vim
   ln -s ~/vimfiles/vimrc ~/.vimrc
   ln -s ~/vimfiles/bashrc ~/.bashrc
# abrir vim e ignorar los errores y warnings varios
# instalar plugins
   :BundleInstall
# reiniciar vim
