CREATE TABLE `template` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='模板';

CREATE TABLE `user` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(50) DEFAULT '' COMMENT '用户名',
  `email` varchar(50) DEFAULT 'example@sse.com.cn' COMMENT '邮箱',
  `phone` varchar(11) DEFAULT '' COMMENT '电话号码',
  `password` varchar(50) DEFAULT NULL COMMENT '密码',
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`name`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='用户';
