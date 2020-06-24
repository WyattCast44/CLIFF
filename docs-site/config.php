<?php

use Illuminate\Support\Str;

return [

    /**
     * General
     */
    'baseUrl' => '',

    'siteName' => 'CLAM',

    'siteDescription' => 'Command Line Applications in Python',

    /**
     * Env
     */
    'production' => false,

    /**
     * Algolia
     */
    'docsearchApiKey' => '',
    'docsearchIndexName' => '',

    /**
     * Nav
     */
    'navigation' => require_once('navigation.php'),

    /**
     * Helpers
     */
    'isActive' => function ($page, $path) {
        return Str::endsWith(trimPath($page->getPath()), trimPath($path));
    },
    'isActiveParent' => function ($page, $menuItem) {
        if (is_object($menuItem) && $menuItem->children) {
            return $menuItem->children->contains(function ($child) use ($page) {
                return trimPath($page->getPath()) == trimPath($child);
            });
        }
    },
    'url' => function ($page, $path) {
        return Str::startsWith($path, 'http') ? $path : '/' . trimPath($path);
    },
];
