;; autor Guillermo Vaya
(add-to-list 'load-path "~/.emacs.d/")  ;; añadimos .emacs.d al path de emacs

(setq-default indent-tabs-mode nil) ;; usa espacios en vez de tabuladores
(setq default-tab-width 4)          ;; 4 espacios por tab

(ido-mode 1)                        ;; ido
(setq ido-enable-flex-matching t)

(global-linum-mode 1)               ;; pon numero de linea

;; si usamos los paquetes de arch, requiere varios
;; ;;;;;;;;;;;;;;;;; PACMAN ;;;;;;;;;;;;;;;;;;;;
;; aur/auto-complete
;; community/emacs-php-mode
;; aur/emacs-scala-mode
;; aur/pymacs
;; aur/python2-ropemacs
;; aur/emacs-yasnipet
;; 
;;:::::::::::::: MELPA ;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; proyectile
;; magit
;;
;; exportar la variable: (en arch, para que use python2)
;; PYMACS_PYTHON=python2
(require 'package)
(setq package-archives '(("gnu" . "http://elpa.gnu.org/packages/")
                         ("marmalade" . "http://marmalade-repo.org/packages/")
                         ("melpa" . "http://melpa.milkbox.net/packages/")))

;;; This was installed by package-install.el.
;;; This provides support for the package system and
;;; interfacing with ELPA, the package archive.
;;; Move this code earlier if you want to reference
;;; packages in your .emacs.
;;(when
;;    (load
;;     (expand-file-name "~/.emacs.d/elpa/package.el"))
(package-initialize)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (wombat)))
 '(inhibit-startup-screen t)
 '(show-paren-mode t))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:inherit nil :stipple nil :background "#242424" :foreground "#f6f3e8" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height 113 :width normal :foundry "unknown" :family "Droid Sans Mono")))))

(add-hook 'shell-mode-hook 'ansi-color-for-comint-mode-on)

(add-to-list 'load-path "/usr/share/emacs/scala-mode")
(require 'scala-mode)
(require 'clojure-mode)

(setq auto-mode-alist
      (append
       '(("\\.py$" . python-mode)  ;; default python para .py
	 ("\\.php$" . php-mode)   ;; default php para .php
     ("\\.scala$" . scala-mode) ;; scala
     ("\\.clj$" . clojure-mode)) ;; clojure
       auto-mode-alist))


;; (require 'auto-complete)          ;; probamos la carga de autocompletado
;; (global-auto-complete-mode t)

(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "/usr/share/emacs/site-lisp/auto-complete/ac-dict")
(ac-config-default)

(require 'pymacs)
(pymacs-load "ropemacs" "rope-")
(setq ropemacs-enable-autoimport t)

(setq python-check-command "pyflakes") ;; ejecutar M-x pyflakes para comprobar el codigo

(add-to-list 'load-path "~/.emacs.d/")  ;; añadimos .emacs.d al path de emacs

(projectile-global-mode)
;; todo
;; yasnippet
(require 'yasnippet) ;; not yasnippet-bundle"
(yas/global-mode 1) ;; or manually load it with yas-global-mode"
(put 'upcase-region 'disabled nil)

(add-to-list 'load-path "/usr/share/ensime/elisp")
(add-to-list 'exec-path "/usr/share/ensime")
(require 'ensime)
(add-hook 'scala-mode-hook 'ensime-scala-mode-hook) ;; load ensime when scala does
(put 'downcase-region 'disabled nil)
