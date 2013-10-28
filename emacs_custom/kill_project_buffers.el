;;; package --- Summary
;;
;;  Custom functions for emacs
;;
;;; Commentary:
;;  Some of this functions may be duplicated in other/better libraries
;;  They are mostly for learning purposes
;;  Although I called it PROJECT-BUFFERS it only checks for the path
;;  to contain some words.

;; Some custom Emacs functions

;;; Code:
(require 'cl)
(defun filter-buffers-by-file-name (partial-path)
  "Return list of buffers which contain PARTIAL-PATH in its filename."
  (remove-if (lambda (x) (or (null (buffer-file-name x))
                          (null (string-match partial-path (buffer-file-name x))))) (buffer-list)))

(defun kill-project-buffers (partial-path)
  "Kill all buffers which contain PARTIAL-PATH."
  (interactive "sPartial name:")
  (let ((kill-list (filter-buffers-by-file-name partial-path)))
    (if (null kill-list)
        (message (format "No buffers matched '%s'" partial-path))
      (if (y-or-n-p (format "Killing %d buffers.  Continue? " (length kill-list)))
        (mapcar 'kill-buffer  kill-list)
        (message "User cancelled")
        )
    )))

(defun reset-project-buffers (partial-path)
  "Reverts all buffers which contain PARTIAL-PATH."
  (interactive "sPartial name:")
  (let ((revert-list (filter-buffers-by-file-name partial-path)))
    (if (null revert-list)
        (message (format "No buffers matched '%s'" partial-path))
      (if (y-or-n-p (format "Revert %d buffers? " (length revert-list)))
          (progn
            (dolist (buff revert-list)
              (with-current-buffer buff
                (revert-buffer t t t)
                ))
            (message (format "Reverted %d buffers." (length revert-list)))
            )
        (message "User cancelled")
        )
      )))

(provide 'kill_project_buffers)
;;; kill_project_buffers ends here
