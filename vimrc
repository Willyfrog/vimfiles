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
" Python mods
Bundle 'klen/python-mode'
Bundle 'python.vim'
Bundle 'python_match.vim'
Bundle 'pythoncomplete'
" Scala
Bundle 'derekwyatt/vim-scala'
" solarized
Bundle 'altercation/vim-colors-solarized'
" varios colores
Bundle 'vim-scripts/Color-Sampler-Pack'

"Settings

set number
set ruler
syntax enable
set nowrap

if has('statusline')
    set laststatus=2
    " Broken down into easily includeable segments
    set statusline=%<%f\    " Filename
    set statusline+=%w%h%m%r " Options
    set statusline+=%{fugitive#statusline()} "  Git Hotness
    set statusline+=\ [%{&ff}/%Y]            " filetype
    set statusline+=\ [%{getcwd()}]          " current dir
    set statusline+=%=%-14.(%l,%c%V%)\ %p%%  " Right aligned file nav info
endif

set backspace=indent,eol,start

"4 espacios por tab
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

"Mostrar caracteres ocultos
set list
set listchars=tab:,.,trail:.,extends:#,nbsp:. " Highlight problematic whitespace

"iluminar todos los patrones que coinciden en la busqueda
set hlsearch
set incsearch
set ignorecase
set smartcase

set pastetoggle=<F4>

set backupdir=~/.vim/_backup//    " where to put backup files
set directory=~/.vim/_temp//      " where to put swap files
set tags=./tags;/,~/.vimtags      " donde poner los tags

"Mappings
" recolocamos leader a º
let mapleader = 'º'
" use :w!! to write to a file using sudo if you forgot to 'sudo vim file'
" (it will prompt for sudo password when writing)
cmap w!! %!sudo tee > /dev/null %
" Map the arrow keys to be based on display lines, not physical lines
map <Down> gj
map <Up> gk

"pep8
let g:pep8_map='<leader>8'
nmap <leader>n :NERDTreeToggle<CR>
map <leader>b :BufferGatorToggle<CR>
nnoremap <silent> <leader>tt :TagbarToggle<CR>
" Fugitive
nnoremap <silent> <leader>gs :Gstatus<CR>
nnoremap <silent> <leader>gd :Gdiff<CR>
nnoremap <silent> <leader>gc :Gcommit<CR>
nnoremap <silent> <leader>gb :Gblame<CR>
nnoremap <silent> <leader>gl :Glog<CR>
nnoremap <silent> <leader>gp :Git push<CR>

"Colores
"256 colores
set t_Co=256
set background=dark
colorscheme xoria256

"eclim
filetype plugin indent on
