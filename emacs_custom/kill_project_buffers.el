;; Some custom emacs functions

(defun filter-buffers-by-file-name (partial-path)
  "return list of buffers which contains 'partial-path' in its filename"
  (remove-if (lambda (x) (or (null (buffer-file-name x))
                          (null (string-match partial-path (buffer-file-name x))))) (buffer-list)))

(defun kill-project-buffers (partial-path)
  "kills all buffers which contains partial-path"
  (interactive "sPartial name:")
  (let ((kill-list (filter-buffers-by-file-name partial-path)))
    (if (null kill-list)
        (message (format "No buffers matched '%s'" partial-path))
      (if (y-or-n-p (format "killing %d buffers" (length kill-list)))
        (kill-some-buffers kill-list)
        (message ("User cancelled"))
        )
    )))

(defun reset-project-buffers (partial-path)
  "Reverts all buffers which contains partial-path"
  (let ((revert-list (filter-buffers-by-file-name partial-path)))
    (if (null revert-list)
        (message (format "No buffers matched '%s'" partial-path))
      (if (y-or-n-p (format "revert %d buffers?" (length revert-list)))
          (progn
            (dolist (buff revert-list)
              (with-current-buffer buff
                (revert-buffer t t t)
                ))
            (message (format "Reverted %d buffers: '%s'" (length revert-list) (mapcar 'buffer-name)))
            )
        (message ("User cancelled"))
        )
      )))
