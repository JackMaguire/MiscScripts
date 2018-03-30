;;; badwolf-theme.el --- Bad Wolf color theme

;; Copyright (C) 2015  Bartłomiej Kruczyk

;; Author: bkruczyk <bartlomiej.kruczyk@gmail.com>
;; Version: 1.2
;; Keywords: themes
;; Package-Requires: ((emacs "24"))
;; URL: https://github.com/bkruczyk/badwolf-emacs

;; This program is free software; you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.

;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.

;;; Commentary:

;; An Emacs port of Steve's Losh theme for Vim:
;; https://github.com/sjl/badwolf

;;; Credits:

;; Steve Losh is creator of the original theme for Vim
;; (https://github.com/sjl/badwolf), on which this Emacs port was
;; based.

;; locojay is creator of the initial Emacs port
;; (https://github.com/locojay/badwolf).

;;; Code:

(deftheme badwolf "Bad Wolf color theme")

(defgroup badwolf nil
  "Badwolf theme customization variables."
  :group 'faces)

(defcustom badwolf-diff-hl-inverse nil
  "Inverse diff-hl faces."
  :type 'boolean
  :group 'badwolf)

(defcustom badwolf-keywords-nobold nil
  "Do not use bold for keywords."
  :type 'boolean
  :group 'badwolf)

(let* ((plain "#f8f6f2")
       (snow "#ffffff")
       (coal "#000000")
       (brightgravel "#d9cec3")
       (lightgravel "#998f84")
       (gravel "#857f78")
       (mediumgravel "#666462")
       (deepgravel "#45413b")
       (deepergravel "#35322d")
       (darkgravel "#242321")
       (blackgravel "#1c1b1a")
       (blackestgravel "#141413")
       (dalespale "#fade3e")
       (dirtyblonde "#f4cf86")
       (taffy "#ff2c4b")
       (saltwatertaffy "#8cffba")
       (tardis "#0a9dff")
       (orange "#ffa724")
       (lime "#aeee00")
       (dress "#ff9eb8")
       (toffee "#b88853")
       (coffee "#c7915b")
       (darkroast "#88633f")

       (bg blackgravel)
       (hl-line darkgravel))

  (custom-theme-set-variables
   'badwolf
   `(notmuch-search-line-faces
     '(("unread" :foreground ,lime)
       ("flagged" :foreground ,tardis)
       ("deleted" :foreground ,taffy :bold t))))

  (custom-theme-set-faces
   'badwolf

   ;; font lock
   `(default ((t (:inherit nil :foreground ,plain :background ,bg))))
   `(font-lock-builtin-face ((t (:foreground ,plain))))
   `(font-lock-comment-face ((t (:foreground ,lightgravel))))
   `(font-lock-comment-delimiter-face ((t (:foreground ,lightgravel))))
   `(font-lock-constant-face ((t (:foreground ,orange))))
   `(font-lock-doc-face ((t (:foreground ,snow))))
   `(font-lock-function-name-face ((t (:foreground ,plain))))
   `(font-lock-keyword-face ((t (:foreground ,taffy ,@(when (not badwolf-keywords-nobold) `(:weight bold))))))
   `(font-lock-string-face ((t (:foreground ,dirtyblonde))))
   `(font-lock-type-face ((t (:foreground ,dress))))
   `(font-lock-variable-name-face ((t (:foreground ,plain))))
   `(font-lock-warning-face ((t (:foreground ,dress :weight bold))))
   `(shadow ((t (:foreground ,mediumgravel))))
   `(success ((t (:foreground ,lime))))
   `(error ((t (:foreground ,dress :weight bold))))
   `(warning ((t (:foreground ,orange))))

   ;; ui
   `(cursor ((t (:background ,tardis))))
   `(region ((t (:foreground nil :background ,deepgravel))))
   `(secondary-selection ((t (:foreground ,darkgravel :background ,tardis))))
   `(fringe ((t (:background ,bg))))
   `(linum ((t (:foreground ,mediumgravel :background ,bg))))
   `(vertical-border ((t (:foreground ,gravel))))
   `(highlight ((t (:foreground ,coal :background ,dalespale))))
   `(escape-glyph ((t (:foreground ,tardis))))
   `(hl-line ((t (:inherit nil :background ,hl-line))))
   `(minibuffer-prompt ((t (:foreground ,plain))))
   `(mode-line ((t (:box nil :foreground ,snow :background "#595959"))))
   `(mode-line-inactive ((t (:box nil :foreground "#848484" :background "#333333"))))
   `(header-line ((t (:inherit mode-line))))
   `(link ((t (:foreground ,lightgravel :underline t))))
   `(link-visited ((t (:inherit link :foreground ,orange))))

   ;; whitespace-mode
   `(trailing-whitespace ((t (:background ,taffy :foreground ,blackestgravel))))
   `(whitespace-trailing ((t (:background ,taffy :foreground ,blackestgravel))))
   `(whitespace-empty ((t :background ,dirtyblonde)))
   `(whitespace-line ((t (:background ,deepergravel :foreground ,dress))))

   `(whitespace-hspace ((t (:foreground ,deepgravel))))
   `(whitespace-space ((t (:foreground ,deepgravel))))
   `(whitespace-tab ((t (:foreground ,deepgravel))))
   `(whitespace-newline ((t (:foreground ,deepgravel))))

   `(whitespace-indentation ((t (:background ,dirtyblonde :foreground ,taffy))))
   `(whitespace-space-after-tab ((t (:background ,dirtyblonde :foreground ,taffy))))
   `(whitespace-space-before-tab ((t (:background ,dirtyblonde :foreground ,taffy))))

   ;; ruler-mode
   `(ruler-mode-default ((t :inherit linum :underline t)))
   `(ruler-mode-column-number ((t (:foreground ,lightgravel :background ,bg :underline ,mediumgravel))))
   `(ruler-mode-fill-column ((t (:foreground ,dirtyblonde :background ,bg :underline ,mediumgravel))))
   `(ruler-mode-goal-column ((t (:inherit 'ruler-mode-fill-column))))
   `(ruler-mode-comment-column ((t (:inherit 'ruler-mode-fill-column))))
   `(ruler-mode-tab-stop ((t (:inherit 'ruler-mode-fill-column))))
   `(ruler-mode-current-column ((t (:foreground ,tardis :background ,bg :underline ,mediumgravel))))
   `(ruler-mode-margins ((t (:inherit ruler-mode-default))))
   `(ruler-mode-fringes ((t (:inherit ruler-mode-default))))
   `(ruler-mode-pad ((t (:inherit ruler-mode-default))))

   ;; search
   `(isearch ((t (:foreground ,coal :background ,dress :bold t))))
   `(isearch-fail ((t (:foreground ,taffy :background ,coal :bold t))))
   `(lazy-highlight ((t (:foreground ,coal :background ,dalespale :bold t))))

   ;; show-paren-mode
   `(show-paren-match ((t (:foreground ,dalespale :background ,bg :bold t))))
   `(show-paren-mismatch ((t (:foreground ,coal :background ,taffy))))

   ;; anzu
   `(anzu-match-1 ((t (:background ,lime :foreground ,coal))))
   `(anzu-match-2 ((t (:background ,dalespale :foreground ,coal))))
   `(anzu-match-3 ((t (:background ,orange :foreground ,coal))))
   `(anzu-mode-line ((t (:foreground ,dress))))
   `(anzu-replace-to ((t (:background ,tardis :foreground ,coal :bold t))))

   ;; rainbow-delimiters
   `(rainbow-delimiters-depth-1-face ((t (:foreground ,mediumgravel))))
   `(rainbow-delimiters-depth-2-face ((t (:foreground ,dalespale))))
   `(rainbow-delimiters-depth-3-face ((t (:foreground ,dress))))
   `(rainbow-delimiters-depth-4-face ((t (:foreground ,orange))))
   `(rainbow-delimiters-depth-5-face ((t (:foreground ,tardis))))
   `(rainbow-delimiters-depth-6-face ((t (:foreground ,lime))))
   `(rainbow-delimiters-depth-7-face ((t (:foreground ,toffee))))
   `(rainbow-delimiters-depth-8-face ((t (:foreground ,saltwatertaffy))))
   `(rainbow-delimiters-depth-9-face ((t (:foreground ,coffee))))
   `(rainbow-delimiters-unmatched-face ((t (:foreground ,taffy))))

   ;; eshell
   `(eshell-prompt ((t (:foreground ,tardis))))

   ;; which-function-mode
   `(which-func ((t :inherit font-lock-function-name-face)))

   ;; company
   `(company-echo-common ((t (:foreground ,plain))))
   `(company-preview ((t (:background ,darkgravel :foreground ,plain))))
   `(company-preview-common ((t (:foreground ,orange))))
   `(company-preview-search ((t (:foreground ,tardis))))
   `(company-scrollbar-bg ((t (:background ,deepgravel))))
   `(company-scrollbar-fg ((t (:background ,mediumgravel))))
   `(company-tooltip ((t (:foreground ,plain :background ,darkgravel))))
   `(company-tooltip-annotation ((t (:foreground ,coffee :background ,darkgravel))))
   `(company-tooltip-common ((t (:foreground ,dress :background ,darkgravel))))
   `(company-tooltip-common-selection ((t (:foreground ,dress :background ,darkgravel))))
   `(company-tooltip-mouse ((t (:inherit highlight))))
   `(company-tooltip-selection ((t (:background ,darkgravel :foreground ,orange))))
   `(company-template-field ((t (:inherit region))))

   ;; ido et al
   `(ido-first-match ((t (:foreground ,orange))))
   `(ido-only-match ((t (:foreground ,dress))))
   `(ido-subdir ((t (:foreground ,plain))))
   `(ido-indicator ((t (:foreground ,lime))))
   `(ido-incomplete-regexp ((t (:foreground ,taffy :weight bold))))

   `(ido-vertical-match-face ((t (:weight normal :underline nil :foreground ,dress))))

   `(flx-highlight-face ((t (:foreground ,dress :weight normal :underline nil))))

  ;; ivy
   `(ivy-confirm-face ((t :foreground ,lime)))
   `(ivy-current-match ((t :bold t :background ,hl-line)))
   `(ivy-match-required-face ((t :foreground ,taffy)))
   `(ivy-minibuffer-match-face-1 ((t :inherit nil)))
   `(ivy-minibuffer-match-face-2 ((t :foreground ,orange)))
   `(ivy-minibuffer-match-face-3 ((t :foreground ,orange)))
   `(ivy-minibuffer-match-face-4 ((t :foreground ,orange)))
   `(ivy-remote ((t :foreground ,tardis)))

   `(swiper-line-face ((t :inherit nil :background ,hl-line)))
   `(swiper-match-face-1 ((t :inherit nil)))
   `(swiper-match-face-2 ((t :foreground ,bg :background ,dalespale :bold t)))
   `(swiper-match-face-3 ((t :foreground ,bg :background ,dress :bold t)))
   `(swiper-match-face-4 ((t :foreground ,bg :background ,tardis :bold t)))

   ;; org
   `(outline-1 ((t (:foreground ,orange :height 1.2))))

   `(org-done ((t (:foreground ,saltwatertaffy :weight bold))))
   `(org-todo ((t (:foreground ,dalespale :weight bold))))
   `(org-date ((t (:foreground ,dress :underline t))))
   `(org-special-keyword ((t (:foreground ,dress))))
   `(org-document-info ((t (:foreground ,brightgravel))))
   `(org-document-title ((t (:foreground ,plain :family "sans" :height 1.8 :weight bold))))

   ;; erc
   `(erc-default-face ((t (:inherit default))))
   `(erc-notice-face ((t (:inherit font-lock-comment-face))))
   `(erc-nick-default-face ((t (:foreground ,taffy :bold t))))
   `(erc-nick-msg-face ((t (:inherit erc-nick-default-face))))
   `(erc-my-nick-face ((t (:foreground ,orange :bold t))))
   `(erc-current-nick-face ((t (:inherit erc-my-nick-face))))
   `(erc-direct-msg-face ((t (:foreground ,snow))))
   `(erc-input-face ((t (:foreground ,dress))))
   `(erc-prompt-face ((t (:foreground ,tardis))))
   `(erc-button ((t (:inherit link))))
   `(erc-timestamp-face ((t (:foreground ,lime))))

   ;; notmuch
   `(notmuch-tag-face ((t (:foreground ,dress))))

   ;; message
   `(message-cited-text ((t :foreground ,dirtyblonde)))
   `(message-header-cc ((t (:foreground ,plain))))
   `(message-header-name ((t (:foreground ,taffy))))
   `(message-header-other ((t (:foreground ,plain))))
   `(message-header-subject ((t (:foreground ,orange))))
   `(message-header-to ((t (:foreground ,plain))))
   `(message-header-xheader ((t (:foreground ,plain))))
   `(message-mml ((t (:foreground ,lightgravel))))

   ;; magit
   `(magit-bisect-bad ((t (:foreground ,taffy))))
   `(magit-bisect-good ((t (:foreground ,lime))))
   `(magit-bisect-skip ((t (:foreground ,orange))))
   `(magit-blame-heading ((t (:foreground ,lightgravel))))
   `(magit-branch-local ((t (:foreground ,orange))))
   `(magit-branch-remote ((t (:foreground ,dress))))
   `(magit-diff-added ((t (:background ,darkgravel :foreground ,lime))))
   `(magit-diff-added-highlight ((t (:background ,deepergravel :foreground ,lime))))
   `(magit-diff-base ((t (:background ,darkgravel :foreground ,dirtyblonde))))
   `(magit-diff-base-highlight ((t (:background ,deepergravel :foreground ,dirtyblonde))))
   `(magit-diff-context ((t (:foreground ,lightgravel))))
   `(magit-diff-context-highlight ((t (:background ,darkgravel :foreground ,brightgravel))))
   `(magit-diff-removed ((t (:background ,darkgravel :foreground ,taffy))))
   `(magit-diff-removed-highlight ((t (:background ,deepergravel :foreground ,taffy))))
   `(magit-diff-lines-boundary ((t (:foreground ,bg :background ,dalespale))))
   `(magit-diff-lines-heading ((t (:background ,dalespale :foreground ,bg))))
   `(magit-diffstat-added ((t (:foreground ,lime :background ,bg))))
   `(magit-diffstat-removed ((t (:foreground ,taffy :background ,bg))))
   `(magit-dimmed ((t (:inherit shadow))))
   `(magit-header-line ((t (:foreground ,dirtyblonde))))
   `(magit-log-author ((t (:foreground ,dirtyblonde))))
   `(magit-log-date ((t (:foreground ,brightgravel))))
   `(magit-process-ng ((t (:inherit error))))
   `(magit-process-ok ((t (:foreground ,lime))))
   `(magit-section-heading ((t (:foreground ,dirtyblonde))))
   `(magit-section-heading-selection ((t (:foreground ,dalespale))))

   ;; diff-hl
   `(diff-hl-insert ((t ,(if badwolf-diff-hl-inverse
                             `(:background ,bg :foreground ,lime)
                           `(:background ,lime :foreground ,bg)))))
   `(diff-hl-delete ((t ,(if badwolf-diff-hl-inverse
                             `(:background ,bg :foreground ,taffy)
                           `(:background ,taffy :foreground ,bg)))))
   `(diff-hl-change ((t ,(if badwolf-diff-hl-inverse
                             `(:background ,bg :foreground ,orange)
                           `(:background ,orange :foreground ,bg)))))))

;;;###autoload
(when load-file-name
  (add-to-list 'custom-theme-load-path
               (file-name-as-directory (file-name-directory load-file-name))))

(provide-theme 'badwolf)

;; Local Variables:
;; no-byte-compile: t
;; End:

;;; badwolf-theme.el ends here
