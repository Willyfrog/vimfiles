set nocompatible
filetype off

set rtp+=~/.vim/bundle/vundle
call vundle#rc()

" vundle's bundle
Bundle 'gmarik/vundle'
" git
Bundle 'tpope/vim-fugitive'
" nerdtree
Bundle 'scrooloose/nerdtree'
" ctrlp
Bundle 'kien/ctrlp.vim'
" Syntastic
Bundle 'scrooloose/syntastic'
" Tagbar
Bundle 'majutsushi/tagbar'
" SuperTab
Bundle 'ervandew/supertab'
" Buffergator
Bundle 'jeetsukumaran/vim-buffergator'
" pythonmode
Bundle 'klen/python-mode'
" solarized
Bundle 'altercation/vim-colors-solarized'
" varios colores
Bundle 'vim-scripts/Color-Sampler-Pack'

"Settings

set number
set ruler
syntax enable
set nowrap

"4 espacios por tab
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

"Mostrar caracteres ocultos
set list

"iluminar todos los patrones que coinciden en la busqueda
set hlsearch
set incsearch
set ignorecase
set smartcase

set backupdir=~/.vim/_backup//    " where to put backup files
set directory=~/.vim/_temp//      " where to put swap files

"Mappings

" use :w!! to write to a file using sudo if you forgot to 'sudo vim file'
" (it will prompt for sudo password when writing)
cmap w!! %!sudo tee > /dev/null %
" Map the arrow keys to be based on display lines, not physical lines
map <Down> gj
map <Up> gk

"Colores
"256 colores
set t_Co=256
set background=dark
colorscheme xoria256
