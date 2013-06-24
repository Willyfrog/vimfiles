(add-to-list 'load-path "~/.emacs.d/el-get/el-get")

(unless (require 'el-get nil 'noerror)
  (with-current-buffer
      (url-retrieve-synchronously
       "https://raw.github.com/dimitri/el-get/master/el-get-install.el")
    (let (el-get-master-branch)
      (goto-char (point-max))
      (eval-print-last-sexp))))

(el-get 'sync)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector ["#242424" "#e5786d" "#95e454" "#cae682" "#8ac6f2" "#333366" "#ccaa8f" "#f6f3e8"])
 '(custom-enabled-themes (quote (wombat)))
 '(inhibit-startup-screen t)
 '(safe-local-variable-values (quote ((virtualenv-default-directory . "/home/gvaya/Proyectos/gigas_api") (virtualenv-workon . ".venv"))))
 '(show-paren-mode t)
 '(tool-bar-mode nil))

;;IDO
(require 'ido)
(ido-mode t)
(setq ido-enable-flex-matching t)
;;Parentesis
(show-paren-mode 1)
(setq show-paren-delay 0)

(setq auto-mode-alist
  (append
    '(("\\.php" . php-mode)
      ("\\.py" . python-mode)
      ("\\.js" . js3-mode)
      ("\\.clj" . clojure-mode)
      ("\\.html" . html-mode)
      ("\\.rst" . rst-mode)
      ("\\.inc$" . php-mode)
    auto-mode-alist)))

;; funcion propia para convertir a 4 espacios
(defun my-php-mode-hook ()
  "My PHP mode configuration. http://stackoverflow.com/questions/12254982/emacs-php-indentation"
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

;; hooks para cargar cosas extra con los modes
(add-hook 'python-mode-hook 'jedi:setup)
(add-hook 'clojure-mode-hook 'paredit-mode)
(add-hook 'shell-mode-hook 'ansi-color-for-comint-mode-on)
(add-hook 'nrepl-mode-hook 'paredit-mode)
(add-hook 'php-mode-hook 'my-php-mode-hook)

(setq-default indent-tabs-mode nil) ;; usa espacios en vez de tabuladores
(setq tab-width 4)          ;; 4 espacios por tab

(require 'auto-complete)          ;; probamos la carga de autocompletado
(global-auto-complete-mode t)

(setq twittering-use-master-password t)

(require 'iso-transl) ;; habilitar acentos
(put 'scroll-left 'disabled nil)

;; shift+direction moves to that window
(when (fboundp 'windmove-default-keybindings)
      (windmove-default-keybindings))

;; php lint
(defun php-lint-file ()
       (interactive)
       (compile (format "php -l %s" (buffer-file-name))))
;; end of php lint
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "Inconsolata" :foundry "unknown" :slant normal :weight normal :height 98 :width normal)))))
