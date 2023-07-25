/*
  Warnings:

  - The values [AROUND,ALL] on the enum `Skill_target` will be removed. If these variants are still used in the database, this will fail.

*/
-- AlterTable
ALTER TABLE `Skill` MODIFY `target` ENUM('NONE', 'SELF', 'ALLY', 'ALLY_SUMMON', 'ALLY_AROUND', 'ALLY_EXCEPT_SELF', 'ENEMY', 'ENEMY_SUMMON', 'ENEMY_AROUND', 'ANY', 'ANY_AROUND', 'ANY_EXCEPT_SELF', 'ANY_SUMMON', 'POINT', 'POINT_ENEMY', 'POINT_ALLY', 'AREA', 'AREA_ENEMY', 'AREA_ALLY') NOT NULL DEFAULT 'ENEMY';
