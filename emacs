;;; package --- Summary
;;
;; .emacs de Guillermo Vayá Pérez guivaya@gmail.com @Driadan
;;
;;; Commentary: 
;;
;; This config file can be copied and modified. 
;; No need to ask for permission or mention author.
;;
;;; Code:

(add-to-list 'load-path "~/.emacs.d/hy-mode")
(require 'hy-mode)

(add-to-list 'load-path "~/.emacs.d/el-get/el-get")

(unless (require 'el-get nil 'noerror)
  (with-current-buffer
      (url-retrieve-synchronously
       "https://raw.github.com/dimitri/el-get/master/el-get-install.el")
    (let (el-get-master-branch)
      (goto-char (point-max))
      (eval-print-last-sexp))))

;; synch packages
(setq my-el-get-packages  
      (append  
       '(auto-complete 
         autopair
         clojure-mode
         cl-lib
         deferred
         jedi
         js3-mode
         json
         magit
         nrepl
         paredit
         php-mode-improved
         pkgbuild-mode
         popup
         python-mode
         rst-mode
         smart-operator
         smarty-mode
         twittering-mode
         virtualenv
         fill-column-indicator
         )))

(el-get 'sync my-el-get-packages)

;; org-mode
(require 'org-install)
(define-key global-map "\C-cl" 'org-store-link)
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)

;; apply some configuration for Mac OS X only
(if (string-equal system-type "darwin")
    (progn 

      ;; option -> alt & command -> meta
      (setq mac-option-modifier nil
            mac-command-modifier 'meta
            x-select-enable-clipboard t)

      ;; Setup PATH in darwin
      (setenv "PATH" (shell-command-to-string "source ~/.bash_profile; echo -n $PATH"))
      ;; Update exec-path with the contents of $PATH
      (loop for path in (split-string (getenv "PATH") ":") do 
            (add-to-list 'exec-path path))

      ;; Grab other environment variables
      (loop for var in (split-string (shell-command-to-string "source ~/.bash_profile; env")) do
            (let* ((pair (split-string var "="))
                   (key (car pair))
                   (value (cadr pair)))
              (unless (getenv key)
                (setenv key value))))
      ))

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector ["#242424" "#e5786d" "#95e454" "#cae682" "#8ac6f2" "#333366" "#ccaa8f" "#f6f3e8"])
 '(custom-enabled-themes (quote (wombat)))
 '(inhibit-startup-screen t)
 '(safe-local-variable-values (quote ((virtualenv-default-directory . "~/Proyectos/gigas_api") (virtualenv-workon . "api") (encoding . utf-8))))
 '(send-mail-function (quote sendmail-send-it))
 '(show-paren-mode t)
 '(tool-bar-mode nil))


;;No tool bar mode
(tool-bar-mode -1)

;;IDO
(require 'ido)
(ido-mode t)
(setq ido-enable-flex-matching t)

;;Parentesis
(show-paren-mode 1)
(setq show-paren-delay 0)

;; set major modes
(add-to-list 'auto-mode-alist '("\\.php\\'" . php-mode))
(add-to-list 'auto-mode-alist '("\\.inc\\'" . php-mode))
(add-to-list 'auto-mode-alist '("\\.py\\'" . python-mode))
(add-to-list 'auto-mode-alist '("\\.rst\\'" . rst-mode))
(add-to-list 'auto-mode-alist '("\\.js\\'" . js3-mode))
(add-to-list 'auto-mode-alist '("\\.clj\\'" . clojure-mode))
(add-to-list 'auto-mode-alist '("\\.html\\'" . html-mode))
(add-to-list 'auto-mode-alist '("\\.hy\\'" . hy-mode))
(add-to-list 'auto-mode-alist '("\\.org\\'" . org-mode))
(add-to-list 'auto-mode-alist '("\\emacs\\'" . emacs-lisp-mode))
(add-to-list 'auto-mode-alist '("\\.el\\'" . emacs-lisp-mode))
(add-to-list 'auto-mode-alist '("\\.lisp\\'" . lisp-mode))
(add-to-list 'auto-mode-alist '("\\.lsp\\'" . lisp-mode))
(add-to-list 'auto-mode-alist '("\\.cl\\'" . lisp-mode))

;; funcion propia para convertir a 4 espacios
(defun my-php-mode-hook ()
  "My PHP mode configuration.  http://stackoverflow.com/questions/12254982/emacs-php-indentation ."
  (setq indent-tabs-mode nil
        tab-width 4
        c-default-style "linux"
        c-basic-offset 4)
  (setq case-fold-search t)
  ;;(setq fill-column 78)
  ;;(c-set-offset 'arglist-cont 0)
  ;;(c-set-offset 'arglist-intro '+)
  (c-set-offset 'case-label 4))
  ;;(c-set-offset 'arglist-close 0))

(defun my-common-lisp-mode-hook ()
  "Common lisp configuration."
  (setq inferior-lisp-program "rlwrap sbcl")
  (add-to-list 'load-path "/usr/share/emacs/site-lisp/slime/")
  (require 'slime)
  (slime-setup)
  (paredit-mode)
  )

(defun my-python-mode-hook ()
  "Python configuration."
  (jedi:setup)
  (setq jedi:setup-keys t)
  (setq jedi:complete-on-dot t)2
  (setq py-shell-switch-buffers-on-execute-p t)
  (setq py-switch-buffers-on-execute-p t)
  (setq py-split-windows-on-execute-p nil)
  (setq py-smart-indentation t)
  )
;; flycheck
;; (add-hook 'after-init-hook #'global-flycheck-mode)
;; hooks para cargar cosas extra con los modes
(add-hook 'python-mode-hook 'my-python-mode-hook)
(add-hook 'clojure-mode-hook 'paredit-mode)
(add-hook 'shell-mode-hook 'ansi-color-for-comint-mode-on)
(add-hook 'nrepl-mode-hook 'paredit-mode)
(add-hook 'php-mode-hook 'my-php-mode-hook)
(add-hook 'hy-mode-hook 'paredit-mode)
(add-hook 'emacs-lisp-mode-hook 'paredit-mode)
(add-hook 'lisp-mode-hook 'my-common-lisp-mode-hook)

(setq-default indent-tabs-mode nil) ;; usa espacios en vez de tabuladores
(setq tab-width 4)          ;; 4 espacios por tab

;; probamos la carga de autocompletado
(require 'auto-complete)
(global-auto-complete-mode t)

(setq twittering-use-master-password t)

;; habilitar acentos
(require 'iso-transl)
(put 'scroll-left 'disabled nil)

;; shift+direction moves to that window
(when (fboundp 'windmove-default-keybindings)
      (windmove-default-keybindings))

;; php lint
(defun php-lint-file ()
  "Lint php files."
       (interactive)
       (compile (format "php -l %s" (buffer-file-name))))
;; end of php lint

;; para que fci este a 80
(setq-default fill-column 80)

;; linea para marcar el ancho que debería mantener
(require 'fill-column-indicator)
(define-globalized-minor-mode
  global-fci-mode fci-mode (lambda () (fci-mode 1)))
(global-fci-mode t)
(setq fci-rule-color "darkblue")


;; my custom functions
(add-to-list 'load-path "~/vimfiles/emacs_custom/")
(load "kill_project_buffers")
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "DejaVu Sans Mono" :foundry "unknown" :slant normal :weight normal :height 98 :width normal)))))

(provide 'emacs)
;;; emacs ends here
