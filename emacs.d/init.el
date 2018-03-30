(setq cc-search-directories '("." "../src" "../../src" "../../../src" "../../../../src" "../../../../../src"))

(when (fboundp 'electric-indent-mode) (electric-indent-mode -1))
;; This is a template emacs initialization file
;;
;; To use, copy all or some to  ~/.emacs.d/init.el

; Enable syntax hilighting
(global-font-lock-mode 1)

;; (global-set-key [\M q] 'query-replace-regexp)


(setq inhibit-splash-screen t)

; short cut keys for compiling
(global-set-key [(f5)] 'compile)
(global-set-key [(f6)] 'recompile)

; like tab expansion for variable names etc.
(global-set-key [f12]         'dabbrev-expand)
(define-key esc-map [f12]     'dabbrev-completion)

; when two buffers are opened with the same name, they have the first
; unique subdirectory appeneded to the end of the buffer name to help
; distinguish the files
(require 'uniquify)
(setq uniquify-buffer-name-style 'reverse)
(setq uniquify-separator "/")
(setq uniquify-after-kill-buffer-p t) ; rename after killing uniquified
(setq uniquify-ignore-buffers-re "^\\*") ; don't muck with special buffers

; ido mode helps quickly open files, switch buffers etc.
; remember:
;   C-f -> go back to normal find-file
;   C-d -> open dired
;   C-j -> create new file (becuase enter would open the closest matching file)
(require 'ido)
(ido-mode t)
(setq ido-enable-flex-matching t)

; put the current function in the bottom buffer
; apl temp -- which-function-mode messes up our long .src.settings python files
; apl temp -- to make them more or less uneditable.
; apl temp -- disable generally -- enable for c++ (which-function-mode t)

; C-c o takes you from the cc file to hh file and visa versa
(add-hook 'c-mode-common-hook
  (lambda()
    (local-set-key  (kbd "C-c o") 'ff-find-other-file)))

;; Your init file should contain only one such instance.
;; If there is more than one, they won't work right.
(custom-set-variables
 '(safe-local-variable-values (quote ((rm-trailing-spaces . t) (show-trailing-whitespace . t) (rm-trailing-spaces . t)))))

; have tabbing in c++ mode work like it should with Rosetta
; if you find a place where it isn't working right
; do C-c C-s and it will tell you what syntax element you are in
; then add a c-set-offset command   -> '+ is one tab stop
(defun my-c++-mode-hook ()
  ;; RosettaCommons Syntax style for C++ code

  (c-set-offset 'arglist-intro '+)
  (c-set-offset 'arglist-close 0)
  (c-set-offset 'arglist-cont-nonempty '+)
  (c-set-offset 'innamespace 0)
  (c-set-offset 'statement-cont '+)
  (c-set-offset 'stream-op '0)

 )

(defun enable-which-function-mode() 
  "set which-function-mode to true"
  (which-function-mode t ))

(add-hook 'c-mode-common-hook 'my-c++-mode-hook)
(add-hook 'c-mode-common-hook 'enable-which-function-mode)


; This hook deletes trailing whitespace, for any file type, in any mode
; upon saving.
; Uncomment to use.
;; (add-hook 'before-save-hook 'delete-trailing-whitespace)

(savehist-mode 1)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(safe-local-variable-values (quote ((show-trailing-whitespace . f) (rm-trailing-spaces . t)))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(setq tab-width 4)

(global-set-key (kbd "C-x <up>") 'windmove-up)
(global-set-key (kbd "C-x <down>") 'windmove-down)
(global-set-key (kbd "C-x <right>") 'windmove-right)
(global-set-key (kbd "C-x <left>") 'windmove-left)
(global-set-key (kbd "M-q") 'query-replace-regexp)

;(add-to-list 'load-path "/usr/share/emacs24/site-lisp/emacs-goodies-el/color-theme.el")
;(require 'color-theme)
;(eval-after-load "color-theme"
;  '(progn
;     (color-theme-initialize)
;     (color-theme-hober)))


(add-to-list 'custom-theme-load-path "$HOME/.emacs.d/themes/")
(load-theme 'badwolf t)
