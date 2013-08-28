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
