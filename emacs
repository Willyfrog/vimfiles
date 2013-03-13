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
 '(show-paren-mode t)
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

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
    auto-mode-alist)))

;; hooks para cargar cosas extra con los modes
(add-hook 'python-mode-hook 'jedi:setup)
(add-hook 'clojure-mode-hook 'paredit-mode)
(add-hook 'shell-mode-hook 'ansi-color-for-comint-mode-on)

(setq-default indent-tabs-mode nil) ;; usa espacios en vez de tabuladores
(setq default-tab-width 4)          ;; 4 espacios por tab

(require 'auto-complete)          ;; probamos la carga de autocompletado
(global-auto-complete-mode t)

(setq twittering-use-master-password t)

(require 'iso-transl) ;; habilitar acentos
